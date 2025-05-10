## Enumeration Methodology

## 1. Giới thiệu

- Có thể hiểu `Enumeration` như là một phần của `Active Recon`, bao gồm các kỹ thuật truy vấn đến các dịch vụ của máy mục tiêu
- Trong đây mình sẽ note về enumeration trong một bức tranh tổng quát nhất

## Các phân lớp chính

![image](https://github.com/user-attachments/assets/3945ca3e-db5a-4a12-8766-2f027c4376f7)

1. **Internet Presence** – Khảo sát mặt bằng Internet công khai.

2. **Gateway** – Xác định biện pháp bảo vệ ở biên mạng.

3. **Accessible Services** – Thống kê dịch vụ và phiên bản đang chạy.

4. **Processes** – Lập bản đồ quy trình và luồng dữ liệu nội bộ.

5. **Privileges** – Liệt kê users, groups và privileges.

6. **OS Setup** – Xác định OS, cấu hình, file nhạy cảm

| **Layer** | **Description** | **Target** | **Information Categories** |
| --- | --- | --- | --- |
| **1. Internet Presence** | Xác định sự hiện diện trên internet và cơ sở hạ tầng có thể truy cập từ bên ngoài. | Xác định tất cả các hệ thống và giao diện mục tiêu có thể kiểm tra | Domains, Subdomains, vHosts, ASN, Netblocks, IP Addresses, Cloud Instances, Security Measures |
| **2. Gateway** | Xác định các biện pháp bảo mật có thể bảo vệ cơ sở hạ tầng bên ngoài và nội bộ của công ty. | Hiểu rằng đang đối mặt với hệ thống gì và cần chú ý những gì | Firewalls, DMZ, IPS/IDS, EDR, Proxies, NAC, Network Segmentation, VPN, Cloudflare |
| **3. Accessible Services** | Xác định các giao diện và dịch vụ có thể truy cập từ bên ngoài hoặc bên trong. | Hiểu lý do và chức năng của hệ thống mục tiêu, đồng thời có được kiến thức cần thiết để giao tiếp và khai thác chúng cho mục đích kiểm thử | Service Type, Functionality, Configuration, Port, Version, Interface |
| **4. Processes** | Xác định các internal processes, sources + destinations liên quan đến các dịch vụ | Xác định được các thành phần trên và hiểu mối quan hệ giữa chúng | PID, Processed Data, Tasks, Source, Destination |
| **5. Privileges** | Xác định internal permissions and privileges đối với các dịch vụ có thể truy cập | Xác định có thể/không thể làm gì với các quyền này | Groups, Users, Permissions, Restrictions, Environment |
| **6. OS Setup** | Xác định các thành phần và cấu hình hệ thống nội bộ | Mục tiêu ở đây là xem cách quản trị viên quản lý các hệ thống và những thông tin nhạy cảm nào mà chúng ta có thể khai thác từ chúng. | OS Type, Patch Level, Network config, OS Environment, Configuration files, sensitive private files |
