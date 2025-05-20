# Pass the Ticket

> Note này giả sử bạn đã biết về giao thức Kerberos trên AD, nếu chưa thì thử tham khảo qua note về [Kerberos](../../../Technology_Fundamental/Protocol/Kerberos.md) của mình nhe

## Giới thiệu chung

Pass the Ticket (PtT) là kỹ thuật tấn công trong môi trường Kerberos, cho phép kẻ tấn công sử dụng lại một **Kerberos ticket hợp lệ** (thường là Ticket Granting Ticket - TGT hoặc Ticket Granting Service - TGS) đã bị đánh cắp để giả mạo người dùng và truy cập các dịch vụ mạng mà không cần mật khẩu.

Kỹ thuật này thường được dùng để di chuyển ngang (lateral movement) trong mạng nội bộ, leo thang đặc quyền (privilege escalation) và duy trì quyền truy cập lâu dài.

---

## Cách có được một ticket hợp lệ

### 1. Trích xuất ticket từ bộ nhớ LSASS

- Khi kẻ tấn công đã chiếm quyền trên một máy tính trong domain (qua phishing, malware, khai thác lỗ hổng...), họ có thể dùng công cụ như **Mimikatz, Rubeus, Kekeo** để trích xuất các ticket Kerberos (TGT hoặc TGS) từ bộ nhớ tiến trình LSASS.  
- Đây là cách phổ biến nhất để lấy ticket hợp lệ mà không cần mật khẩu.

### 2. Kerberoasting
- Kẻ tấn công dùng tài khoản hợp lệ để yêu cầu service ticket cho các tài khoản dịch vụ trong domain.  
- Service ticket được mã hóa bằng khóa mật khẩu tài khoản dịch vụ.  
- Kẻ tấn công lấy ticket về và brute-force để tìm mật khẩu tài khoản dịch vụ, từ đó có thể tạo hoặc sử dụng ticket hợp lệ.

### 3. Golden Ticket
- Khi có quyền quản trị trên Domain Controller, kẻ tấn công có thể dump hash mật khẩu tài khoản **KRBTGT**.  
- Dùng hash này tạo **Golden Ticket** giả mạo với quyền truy cập toàn bộ domain, tồn tại lâu dài.

### 4. Các kỹ thuật khác
- Lấy ticket từ các máy chủ có delegation không an toàn.  
- Khai thác lỗ hổng cấu hình hoặc lỗi Kerberos để tạo hoặc chỉnh sửa ticket.

---

## Cách thực hiện kỹ thuật Pass the Ticket

### Bước 1: Chuẩn bị ticket
- Lấy ticket hợp lệ (TGT hoặc TGS) từ bộ nhớ LSASS hoặc tạo ticket giả mạo.

### Bước 2: Chèn (inject) ticket vào phiên làm việc

- Dùng công cụ như **Mimikatz** hoặc **Rubeus** để chèn ticket vào phiên đăng nhập hiện tại của kẻ tấn công.  
- Ví dụ lệnh Mimikatz:  
```
kerberos::ptt ticket.kirbi
```

### Bước 3: Sử dụng ticket để truy cập dịch vụ

- Sau khi chèn ticket, kẻ tấn công có thể truy cập các tài nguyên mạng với quyền của người dùng bị đánh cắp ticket mà không cần mật khẩu.  
- Có thể dùng ticket để yêu cầu thêm service ticket (TGS) mới từ KDC hoặc truy cập trực tiếp dịch vụ.

---

## Các điểm cần lưu ý

- Pass the Ticket không cần mật khẩu người dùng, chỉ cần ticket hợp lệ.  
- Ticket có thời hạn (thường 10 giờ) nên kẻ tấn công phải sử dụng trong khoảng thời gian này hoặc tạo Golden Ticket để kéo dài thời gian.  
- Kỹ thuật này rất khó phát hiện vì các ticket được hệ thống tin tưởng và hoạt động như người dùng thật.

---

## Tham khảo

- [Netwrix Pass the Ticket](https://www.netwrix.com/pass_the_ticket.html)  
- [BeyondTrust Pass the Ticket](https://www.beyondtrust.com/resources/glossary/what-are-pass-the-ticket-attacks)  
- [MITRE ATT&CK T1550.003](https://www.picussecurity.com/resource/blog/t1550.003-pass-the-ticket-adversary-use-of-alternate-authentication)  
- [Twingate Pass the Ticket](https://www.twingate.com/blog/glossary/pass%20the%20ticket)