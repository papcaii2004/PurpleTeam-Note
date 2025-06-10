# C2 Infrastructure

> Lần đầu mình host C2 server trên VPS và đã bị quét vài ngày sau đó, mình nhận ra là build C2 server không chỉ đơn giản là run server trên VPS mà còn là setup sao cho tránh khỏi việc bị phát hiện. Và đó chính là mục tiêu của note này

## Kiến trúc hạ tầng

Điểm cốt lõi là hệ thống C2 này sẽ là một hệ thống đa tầng, thay vì chỉ một server như trước mình làm, bao gồm:

- **Cloudflare Proxy:** Để obfuscate lưu lượng mạng thông qua DNS

- **NGINX Proxy VPS:** Đóng vai như một `re-director`. đảm bảo mọi traffic được kiểm soát trước khi đến C2 server

- **Sliver C2 VPS:** C2 server của chúng ta, chịu trách nhiệm handle các request sau khi đã đi qua proxy

**Design overview:** Các Lưu lượng mạng đến một tên miền chim mồi (giả sử `vulnlab.com`) được control với **Cloudflare** sẽ được forward đến **Proxy VPS**, sau đó mới đến **C2 VPS**

## Setup

Hiểu kiến trúc rồi bắt tay vào setup thôi

### I/ Config Domain với Cloudflare 

- Đầu tiên ta cần mua một Domain (tùy bạn chọn provider nhe)
- Sau đó vào [Cloudflare Dashboard](https://dash.cloudflare.com/) -> Add a Domain
- Sau khi thêm vào rồi thì ta cần setup NS record để trỏ về Name server của Cloudflare, bước này thì tùy vào Provider bạn chọn để mua domain sẽ có các dashboard để thay đổi NS record khác nhau
- Thêm A Record trỏ đến IPv4 của **Proxy VPS**

### II/ Setup Proxy VPS

#### 1. Tạo SSL Certificate (for HTTPs)

```sh
sudo apt install certbot python3-certbot-nginx
certbot certonly --standalone -d vulnlab.com -m test@vulnlab.com --agree-tos --staple-ocsp
```

- Sau đó có file filechain.pem (Certificate) và privkey.pem (Certificate key) được tạo, 2 file này sẽ được thêm vào Nginx thông qua GUI (ở bước tiếp sau)

#### 2. Cài đặt Docker và Docker Compose

```sh
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### 3. Tạo Container cho Nginx

- Tạo file docker-compose.yml

```docker
version: '3.8'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      # These ports are in format <host-port>:<container-port>
      - '80:80' # Public HTTP Port
      - '443:443' # Public HTTPS Port
      - '81:81' # Admin Web Port
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
```

- Host lên thôi

```sh
docker-compose up -d
```

#### 4. Đăng nhập vào Nginx GUI và thêm rule proxy

- Đăng nhập vào `https://{PROXY_VPS_IP}:81` với cred
	- username: admin@example.com
	- password: changeme

- Thêm Certificate ta có được ở trên
- Thêm rule proxy, điều hướng mọi connections sử dụng domain của ta (config ở trên bằng Cloudflare) đến **C2 VPS**

### III/ Setup C2 VPS

Ở đây mình sẽ sử dụng `Sliver` - một C2 framework rất tiện lợi, cách sử dụng mình có viết trong folder sliver

#### 1. Cài đặt Sliver Server

- Cài đặt sliver server từ repo

```sh
sudo wget https://github.com/BishopFox/sliver/releases/download/v1.5.42/sliver-server_linux
mkdir /opt/sliver
mv sliver-server_linux /opt/sliver/sliver-server_linux
chmod +x /opt/sliver/sliver-server_linux 
sudo /opt/sliver/sliver-server_linux
```

- Ngoài ra, ta nên đổi config để obfuscate patterns của Sliver, nằm ở `~/.sliver/configs/http-c2.json`

- Cài đặt apache2 server để host payload (sẽ được tải thông qua dropper)

```sh
sudo apt update && sudo apt install apache2
```

#### 2. Config Firewall

- Tất nhiên rồi, ta cần lọc traffic đến **C2 VPS** (chỉ nhận packet đến từ **Proxy VPS**)

```sh
#1.  Allow traffic from a specific IP on port 80 and 443
sudo iptables -A INPUT -p tcp -s [PROXY_VPS_IP] --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -s [PROXY_VPS_IP] --dport 443 -j ACCEPT

#2.  before dropping packets, i want to log any drop to see who want to access my machine 
sudo iptables -A INPUT -p tcp --dport 80 -j LOG --log-prefix "IPTABLES-DROP-PORT80: " --log-level 4
sudo iptables -A INPUT -p tcp --dport 443 -j LOG --log-prefix "IPTABLES-DROP-PORT443: " --log-level 4

# 3. Add Rules to Drop Traffic from All Other IPs for port 80 and 443 
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
sudo iptables -A INPUT -p tcp --dport 443 -j DROP
```

### IV/ Viết dropper nào