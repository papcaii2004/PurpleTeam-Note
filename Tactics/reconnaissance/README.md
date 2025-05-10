# Reconnaissance

## 1. Overview

### Recon là gì ?

Loại Recon | Mô tả | Ví dụ
| -------- | ----- | ------ |
Passive Recon | Thu thập thông tin mà không tiếp xúc trực tiếp với hệ thống mục tiêu | Google dorking, LinkedIn mining, tìm kiếm trên Shodan |
Active Recon | Gửi truy vấn trực tiếp tới mục tiêu, có khả năng bị phát hiện | Ping sweep, port scanning, vulnerability scanning |

> Ở trong scope này mình sẽ chỉ tập trung chính vào `Active Recon`

### Mục tiêu chính của Recon

- **Xác định phạm vi & giới hạn:** Biết rõ hệ thống, dịch vụ, và dải IP hợp lệ để thử nghiệm, tránh vi phạm phạm vi cho phép 

- **Tạo bản đồ tấn công (Attack Surface Map)**: Liệt kê host sống, port mở, subdomain, và điểm tiếp xúc giữa network và ứng dụng 

- **Hiểu kiến trúc và hệ thống phòng thủ:** Phát hiện tường lửa, IDS/IPS, WAF, VPN để định hướng cách thức tiếp cận 

- **Chuẩn bị cho các giai đoạn sau:** Cung cấp đầu vào cho scanning, vulnerability assessment, exploitation… 

- Tham khảo mô hình tổng quát trong [Methodology.md](./Methodology.md)

## 2. Các thông tin cần thu thập

### 2.1 Thông tin hạ tầng & mạng
- Host & Port: Quét toàn dải IP, xác định port và dịch vụ đang nghe (Nmap, Masscan).

- Cấu trúc mạng: Dùng traceroute/pathping để thấy topology, phân vùng DMZ vs LAN.

- DNS & Subdomains: Zone transfer (dig AXFR), subdomain bruteforce (dnsenum, fierce) và certificate logs 

### 2.2 Thông tin dịch vụ & version
- Banner grabbing: Nmap -sV, Netcat, curl -I để hiển thị phiên bản phần mềm 

- Fingerprint ứng dụng: HTTP headers, công cụ như WhatWeb, Wappalyzer cho web; smbclient, enum4linux cho SMB 


### 2.3 Thông tin về lỗ hổng & cấu hình
- Vulnerability scanning: OpenVAS, Nessus, Nmap NSE scripts để tìm CVE đã biết

- Misconfiguration: Kiểm tra default creds, directory listing, open S3 buckets…

## 3. Quy trình Active Recon (PTES/NIST overlap)

1. **Target Identification:** Xác định IP, domain, cloud instances 

2. **Port & Service Discovery:** Nmap/Masscan quét port, banner grabbing 

3. **Service Enumeration:** Liệt kê chi tiết services (SMB, SSH, LDAP, SNMP) và cấu hình 

4. **Web Application Recon:** Directory brute-forcing (Gobuster), fingerprint CMS, API 

5. **Vulnerability Lookup:** Dò CVE qua scanners & manual research, mapping to attack chains.

6. **Documentation:** Lưu mọi kết quả, ảnh chụp, log để hỗ trợ scripting và báo cáo

## 3. Cấu trúc thư mục

Trong tài liệu này mình sẽ bao quát Recconaissance theo các bước trong quy trình

```bash
│   Methodology.md                      # Bức tranh tổng quan
│   README.md                           
│
├───01_Target_Identification            
├───02_Port_and_Service_Discovery
├───03_Service_Enumeration
├───04_Web_Application_Recon
├───05_Vulnerability_Lookup
└───06_Documentation_and_Reporting
```
