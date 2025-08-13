# Reconnaissance

## 1. Overview

### Recon là gì ?

Loại Recon | Mô tả | Ví dụ
| -------- | ----- | ------ |
Passive Recon | Thu thập thông tin mà không tiếp xúc trực tiếp với hệ thống mục tiêu | Google dorking, LinkedIn mining, tìm kiếm trên Shodan |
Active Recon | Gửi truy vấn trực tiếp tới mục tiêu, có khả năng bị phát hiện | Ping sweep, port scanning, vulnerability scanning |

> Ở trong scope này mình sẽ chỉ tập trung chính vào `Active Recon`

### Mục tiêu chính của Recon

- **Xác định phạm vi & giới hạn:** Biết rõ hệ thống, dịch vụ, và dải IP hợp lệ để thử nghiệm, tránh vi phạm phạm vi cho phép.
- **Tạo bản đồ tấn công (Attack Surface Map):** Liệt kê host sống, port mở, subdomain, và điểm tiếp xúc giữa network và ứng dụng.
- **Hiểu kiến trúc và hệ thống phòng thủ:** Phát hiện tường lửa, IDS/IPS, WAF, VPN để định hướng cách thức tiếp cận.
- **Chuẩn bị cho các giai đoạn sau:** Cung cấp đầu vào cho scanning, vulnerability assessment, exploitation.
- **OSINT:** Bổ sung thông tin từ nguồn công khai như social media, breach database, WHOIS, certificate logs… để hỗ trợ Active Recon.

---

## 2. Các thông tin cần thu thập

### 2.1 Passive Recon (OSINT)
- **Thông tin định danh cá nhân / tổ chức**
  - Email, số điện thoại, username, tên nhân viên.
  - Tool: [email2phonenumber](https://github.com/martinvigo/email2phonenumber), theHarvester, Hunter.io.
- **Thông tin hạ tầng**
  - Domain & subdomain: crt.sh, SecurityTrails, Amass (passive mode).
  - WHOIS & DNS records (nslookup, whois.domaintools.com).
- **Dữ liệu rò rỉ**
  - Breach data: HaveIBeenPwned, DeHashed.
  - Paste sites: pastebin, ghostbin.
- **Thông tin trên mạng xã hội**
  - LinkedIn, Twitter/X, Facebook, GitHub.
  - Kỹ thuật: profile mining, ảnh, metadata.

---

### 2.2 Active Recon

#### 2.2.1 Thông tin hạ tầng & mạng
- Host & Port: Quét toàn dải IP, xác định port và dịch vụ đang nghe (Nmap, Masscan).
- Cấu trúc mạng: Dùng traceroute/pathping để thấy topology, phân vùng DMZ vs LAN.
- DNS & Subdomains: Zone transfer (dig AXFR), subdomain bruteforce (dnsenum, fierce), certificate logs.

#### 2.2.2 Thông tin dịch vụ & version
- Banner grabbing: `nmap -sV`, Netcat, `curl -I`.
- Fingerprint ứng dụng: HTTP headers, WhatWeb, Wappalyzer; `smbclient`, `enum4linux` cho SMB.

#### 2.2.3 Thông tin về lỗ hổng & cấu hình
- Vulnerability scanning: OpenVAS, Nessus, Nmap NSE scripts.
- Misconfiguration: Default creds, directory listing, open S3 buckets…

---

## 3. Quy trình Active Recon (PTES/NIST overlap)

1. **Passive Recon (OSINT)**  
   Thu thập thông tin từ nguồn công khai, không tương tác trực tiếp.
2. **Target Identification**  
   Xác định IP, domain, cloud instances.
3. **Port & Service Discovery**  
   Nmap/Masscan quét port, banner grabbing.
4. **Service Enumeration**  
   Liệt kê services (SMB, SSH, LDAP, SNMP) và cấu hình.
5. **Web Application Recon**  
   Directory brute-forcing (Gobuster), fingerprint CMS, API.
6. **Vulnerability Lookup**  
   Dò CVE qua scanners & manual research, mapping to attack chains.
7. **Documentation**  
   Lưu kết quả, ảnh chụp, log.

## 3. Cấu trúc thư mục

Trong tài liệu này mình sẽ bao quát Recconaissance theo các bước trong quy trình

```bash
│   Methodology.md                      # Bức tranh tổng quan
│   README.md                           
│
├───00_OSINT                            # OSINT, passive recon
├───01_Target_Identification            
├───02_Port_and_Service_Discovery
├───03_Service_Enumeration
├───04_Web_Application_Recon
├───05_Vulnerability_Lookup
└───06_Documentation_and_Reporting
```
