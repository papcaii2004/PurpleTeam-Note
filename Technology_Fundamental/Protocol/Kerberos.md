
# Kerberos

> Mặc dù giao thức này có thể ứng dụng trong nhiều case khác nhau, nhưng note này sẽ tập trung vào môi trường `Active Directory`

![image](https://github.com/user-attachments/assets/d7c20032-1048-4e87-9151-0c83a7506fc9)

## 1. Kerberos là gì

- Đây là một **Giao thức xác thực** computer-network dựa trên cơ chế tickets

- Trong môi trường `Active Directory (AD)`, Kerberos là giao thức xác thực **mặc định**, cung cấp cơ chế xác thực an toàn cho người dùng, máy tính và dịch vụ trong domain

## 2. Nguyên lý giao thức

### Các thành phần chính

- **Client (Principal):** Người dùng hoặc máy tính yêu cầu truy cập dịch vụ.

- **KDC:** Máy chủ trung gian xác thực và cấp vé (ticket).

	- **Authentication Service (AS):**

		- Xác thực người dùng

		- Cấp Ticket Granting Ticket (TGT)

	- **Ticket-Granting Service (TGS):**

		- Nhận TGT từ client

		- Và trả về TGS tương ứng với service yêu cầu

- **Service Server:** Máy chủ cung cấp dịch vụ mà client muốn truy cập.

![enter image description here](https://miro.medium.com/v2/resize:fit:1400/1*t5vk4uW18Rs0CB_lJJvBvw.png)

| Thành phần | Vai trò trong AD Kerberos |

| ------------------------ | ------------------------------------------------------------------------------------------- |
||  |
|--|--|
|  |  |

---

## 3. Quy trình xác thực Kerberos trong AD 

### Bước 1: Client gửi yêu cầu TGT (AS_REQ) 

- Khi người dùng đăng nhập vào máy Windows, **LSASS** trên client sẽ thu thập thông tin đăng nhập (username, mật khẩu).
- **LSASS** tạo một yêu cầu xác thực (AS_REQ) gửi đến KDC (thường là Domain Controller) để xin cấp TGT. 
- Yêu cầu này bao gồm tên người dùng, tên realm (domain), timestamp và các thông tin cần thiết.
- Yêu cầu này chưa được mã hóa vì client chưa có session key. 

### Bước 2: DC cấp TGT (AS_REP) - DC xác thực thông tin user/computer. 

- Tạo **Ticket Granting Ticket (TGT)**, mã hóa bằng **private key** của KDC. 
- Tạo **session key**, mã hóa bằng khóa được sinh từ mật khẩu user/computer.
- LSASS trên client nhận TGT và session key, lưu trữ trong bộ nhớ để dùng cho các bước xác thực tiếp theo.
- Khi client muốn truy cập dịch vụ khác, LSASS sử dụng TGT để gửi yêu cầu lấy Service Ticket (TGS) từ KDC mà không cần nhập lại mật khẩu.

### Bước 3: Client yêu cầu Service Ticket (TGS_REQ) 

- Khi muốn truy cập dịch vụ, ví dụ SMB của server windows-02 (TGT ticket sẽ là `cifs/windows10-02.ppt.local`), client gửi TGT và **Authenticator** đến TGS trên DC. 
- Authenticator chứa thông tin chứng minh quyền sở hữu TGT, được mã hóa bằng session key. 

### Bước 4: DC cấp Service Ticket (TGS_REP) 

- TGS kiểm tra TGT và Authenticator, nếu hợp lệ cấp **Service Ticket** cho dịch vụ. 
- Service Ticket được mã hóa bằng khóa bí mật của dịch vụ (được lưu trong AD). 
- Client nhận Service Ticket và session key dịch vụ. 

### Bước 5: Client truy cập dịch vụ (AP_REQ) 

- Client gửi Service Ticket và Authenticator đến máy chủ dịch vụ. 
- Máy chủ dịch vụ giải mã Service Ticket, xác thực client dựa trên vé. 
- Nếu hợp lệ, cho phép truy cập. 

### Bước 6: Xác nhận dịch vụ (AP_REP) (tuỳ chọn) 

- Máy chủ dịch vụ gửi phản hồi xác nhận client, hoàn tất xác thực hai chiều. 

![image](https://github.com/user-attachments/assets/8593f766-86bd-49bf-81fa-60453be056ac)

---

## 4. Đặc điểm quan trọng trong AD 
- **TGT có thời hạn mặc định 10 giờ**, có thể renew đến 7 ngày (tuỳ cấu hình domain). 
- **SPN phải chính xác** để Kerberos cấp vé đúng dịch vụ. Sai SPN gây lỗi xác thực. 
- **Delegation** cho phép máy tính hoặc dịch vụ đại diện user truy cập dịch vụ khác, là điểm then chốt trong bảo mật AD. 
- **Single Sign-On (SSO):** Người dùng đăng nhập một lần, có thể truy cập nhiều dịch vụ mà không cần nhập lại mật khẩu. 
---

## Tham khảo 
- [Microsoft Docs – Kerberos Authentication](https://docs.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview) 
- [Red Team Notes – Kerberos in AD](https://dmcxblue.gitbook.io/red-team-notes/active-directory/introduction/kerberos) 
- [TechNet – Service Principal Names](https://docs.microsoft.com/en-us/windows/win32/ad/service-principal-names)
