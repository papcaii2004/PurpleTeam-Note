# Leo thang đặc quyền (Privilege Escalation)

Phần này khá liên quan đến công việc trước của tôi với vai trò là nhà nghiên cứu, và hiện tại chỉ tập trung vào môi trường Windows OS. :))) Tôi sẽ cập nhật các nền tảng khác khi tìm hiểu xong.

## Đây là gì
Leo thang đặc quyền là một trong những bước quan trọng nhất trong một cuộc tấn công mạng. Kỹ thuật này liên quan đến việc khai thác lỗ hổng hệ thống, cấu hình sai, hoặc điểm yếu trong phân quyền người dùng. Nếu thành công, kẻ tấn công có thể nâng từ mức quyền hạn thấp (ví dụ: người dùng thông thường) lên mức cao hơn (ví dụ: quản trị viên hoặc root).

## Vector tấn công
Sau khi đã bao quát hầu hết các kỹ thuật từ MITRE, mình nghĩ nên chia theo một số vector tấn công phổ biến:

### 1. Khai thác lỗ hổng phần mềm  
- **T1068** Exploitation for Privilege Escalation  
- Ví dụ, zero-day driver, buffer overflow…

### 2. Lạm dụng cơ chế kiểm soát  
- **T1548** Abuse Elevation Control Mechanism  
- UAC bypass, registry run keys…

### 3. Thao tác Access Token  
- **T1134** Access Token Manipulation  
- Token theft, impersonation…

### 4. Khai thác dịch vụ/misconfig  
- Exploit IIS, MSSQL misconfig…

## Tài liệu tham khảo
