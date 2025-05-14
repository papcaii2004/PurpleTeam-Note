# Initial Access

> Thực ra lúc ban đầu mình tưởng phase này không quan trọng, nhưng sau khi học và có thêm kinh nghiệm mình mới nhận ra là đây là một bước quan trọng, không thể thiếu trong quá trình Red Team, vậy nó là gì

## Khái niệm

- Đây là một bước được triển khai sau giai đoạn tìm thông tin và chuẩn bị công cụ, nơi mà ta sẽ tìm những đường thâm nhập vào hệ thống của mục tiêu. 
- Nếu bước này không thành công thì ta không thể làm gì được tiếp cả
- Mục tiêu thường là có shell hoặc thực thi được phần mềm (mã độc) trên máy mục tiêu

## Các hướng initial access

- **Phishing:** Email giả mạo, tin nhắn lừa đảo để dụ người dùng tải malware hoặc cung cấp thông tin đăng nhập.

- **Khai thác lỗ hổng phần mềm (Exploits):** Tận dụng các lỗ hổng chưa được vá như Log4j, CVE mới để truy cập trái phép.

- **Dịch vụ truy cập từ xa (External Remote Services):** VPN, Citrix, RDP, các dịch vụ từ xa có cấu hình sai hoặc bị lộ thông tin đăng nhập.

- **Credential Stuffing / Password Spraying:** Sử dụng tài khoản bị rò rỉ hoặc đoán mật khẩu để truy cập hệ thống.

- **Drive-by Download:** Lây nhiễm malware qua trang web bị tấn công mà người dùng không hay biết.