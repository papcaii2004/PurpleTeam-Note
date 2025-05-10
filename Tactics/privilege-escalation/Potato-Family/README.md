# Privilege Escalation: Token Impersonate

## Nguyên lý

- Đây là các kỹ thuật sử lạm dụng các quyền có sẵn để **đánh cắp** hoặc **tái sử dụng** token của một tiến trình cao
- Từ đó khởi tạo tiến trình mới để có quyền cao hơn, điển hình ở đây là các tool `Potato`

### Requirement

- Hầu hết đều cần quyền có sẵn: `SeImpersonatePrivilege` hoặc `SeAssignPrimaryTokenPrivilege`
-> Tại sao lại cần những quyền này ?
- Vì những user với quyền đó có thể được cho phép **giả mạo (impersonate)** token bảo mật của người dùng hoặc dịch vụ khác sau khi người đó xác thực thành công
- Điều này giúp kẻ tấn công có thể "mượn" quyền của tài khoản có đặc quyền cao mà không cần phải biết mật khẩu hay chi tiết đăng nhập.

### How it work

> Vậy các kỹ thuật Potato hoạt động như nào
- Đầu tiên chúng sẽ exploit các lỗ hổng relay NTLM, spoofing hoặc các cơ chế impersonation của Windows để bắt token của một process có quyền cao
- Sau đó sử dụng API như `ImpersonateNamedPipeClient` để mạo danh token mà không cần can thiệp trực tiếp vào kernel (cần quyền `SeImpersonatePrivilege` để sử dụng các API đó)  

### Một chút bên lề

- Trước khi mình học các CVE bên Windows thì thấy việc token impersonate là một kỹ thuật rất phổ biến được sử dụng trong kernel exploit
- Ban đầu mình tưởng 2 token này là khác nhau nhưng hóa ra chúng là một
- Chỉ khác là ở các Kernel exploit sẽ trực tiếp ghi đè con trỏ `_TOKEN` trong struct `_EPROCESS ` ở kernel
- Còn ở đây thì là một kỹ thuật user-mode, tận dụng quyền có sẵn và API impersonation hợp lệ của Windows

## Potato Family

- Trước đến giờ có nhiều công cụ, về bản chất đều lợi dụng cơ chế như trên (được đặt tên là ...Potato, mình cũng không biết sao họ đặt tên đó nữa)
- Tuy đều dựa theo nguyên lý gốc trên, nhưng cách chúng lợi dụng các structure hay API khác nhau cũng khiến chúng hoạt động khác biệt
- Vậy nên phần này sẽ như một cheatsheet để phân loại chúng

#### BadPotato
#### GodPotato
#### DeadPotato

## Tham khảo
- **[Potato Family](https://jlajara.gitlab.io/Potatoes_Windows_Privesc):** Một bài viết khá hay về nhiều loại Potato khác nhau
