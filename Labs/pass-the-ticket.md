# Lab for Pass the Ticket (PtT)

> Đây là cách setup môi trường cho kỹ thuật **Pass the Ticket**

## 1. Chuẩn bị phần mềm và tài nguyên

- Phần mềm ảo hóa: VMware Workstation/Fusion hoặc VirtualBox.

- File ISO cài đặt Windows Server (2016 trở lên) để làm Domain Controller (DC).

- File ISO Windows 10/11 hoặc Windows Server để làm máy client.

- Tối thiểu 8GB RAM cho máy thật để chạy 2 máy ảo mượt (mỗi máy ảo cấp ~4GB RAM).

- Mạng ảo (Virtual Network) cấu hình dạng Internal Network hoặc Host-only để các máy ảo có thể kết nối với nhau.

## 2. Tạo máy ảo Domain Controller (máy chủ AD)

- Tạo máy ảo mới, cài Windows Server 2016/2019/2022.

- Cấu hình IP tĩnh (ví dụ: 192.168.100.10).

- Cài đặt và cấu hình Active Directory Domain Services (AD DS) để tạo domain (ví dụ: lab.local).

- Đặt tên máy (ví dụ: DC1).

- Khởi động lại máy sau khi cài đặt AD.

## 3. Tạo máy ảo client (máy trạm)

- Tạo máy ảo mới, cài Windows 10/11 hoặc Windows Server (client).

- Cấu hình IP tĩnh trong cùng subnet với DC (ví dụ: 192.168.100.20).

- Join máy client vào domain lab.local.

- Đặt tên máy (ví dụ: CLIENT1).

## 4. Tạo tài khoản người dùng domain

- Trên DC, mở Active Directory Users and Computers.

- Tạo tài khoản người dùng domain (ví dụ: user1 với mật khẩu Passw0rd!).

- Cấp quyền user bình thường.


## 5. Quy trình demo Pass the Ticket

- Đăng nhập máy client bằng tài khoản user1.

- Trên máy client, dùng tài khoản admin (hoặc quyền cao) để chạy công cụ như Mimikatz hoặc Rubeus.

- Dùng Mimikatz để dump ticket Kerberos (TGT hoặc TGS) từ bộ nhớ LSASS.

- Lưu ticket ra file .kirbi.

- Dùng Mimikatz hoặc Rubeus để chèn (inject) ticket vào phiên làm việc (kerberos::ptt).

- Sử dụng ticket để truy cập tài nguyên mạng hoặc chạy lệnh với quyền của user bị giả mạo.