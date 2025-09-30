# Multi-Tier C2 Infrastructure Setup  
  
## Architecture Overview  
  
The multi-tier architecture implements defense-in-depth principles through three distinct layers:  
  
1. **Cloudflare Proxy Layer**: DNS-based traffic obfuscation  
2. **NGINX Proxy Layer**: Traffic redirection and SSL termination    
3. **C2 Server Layer**: Payload handling and session management  
  
## Component Setup  
  
### Domain and DNS Configuration  
  
#### Prerequisites  
- Registered domain name  
- Cloudflare account with DNS management  
  
#### Configuration Steps  
  
1. **Domain Registration**  
   - Register domain through preferred provider  
   - Configure nameservers to point to Cloudflare  
  
2. **Cloudflare DNS Setup**  
   ```bash  
   # Access Cloudflare Dashboard  
   https://dash.cloudflare.com/  
     
   # Add domain and configure DNS records  
   A Record: @ -> [PROXY_VPS_IP]
   ```

### NGINX Proxy VPS Setup
 
#### SSL Certificate Generation

```bash
sudo apt install certbot python3-certbot-nginx  
certbot certonly --standalone -d yourdomain.com -m admin@yourdomain.com --agree-tos --staple-ocsp
```

#### Docker Environment Setup

```bash
sudo apt update  
sudo apt install -y docker.io  
sudo systemctl enable docker  
sudo systemctl start docker  
sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
sudo chmod +x /usr/local/bin/docker-compose
```

#### NGINX Proxy Manager Deployment

```bash
# docker-compose.yml  [header-3](#header-3)
version: '3.8'  
services:  
  app:  
    image: 'jc21/nginx-proxy-manager:latest'  
    restart: unless-stopped  
    ports:  
      - '80:80'     # Public HTTP Port  
      - '443:443'   # Public HTTPS Port    
      - '81:81'     # Admin Web Port  
    volumes:  
      - ./data:/data  
      - ./letsencrypt:/etc/letsencrypt
```

#### Proxy Configuration
1. Access admin interface: https://[PROXY_VPS_IP]:81
2. Default credentials: admin@example.com / changeme
3. Upload SSL certificates (fullchain.pem, privkey.pem)
4. Configure proxy rules to forward traffic to C2 server