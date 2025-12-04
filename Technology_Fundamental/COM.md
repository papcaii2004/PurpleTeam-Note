# Component Object Model (COM)

## 1. COM là gì?

**Component Object Model (COM)** là một tiêu chuẩn giao diện nhị phân, độc lập ngôn ngữ, được Microsoft phát triển để cho phép các thành phần phần mềm (gọi là "đối tượng" - object) có thể tương tác với nhau.

Hãy tưởng tượng COM như một hệ thống **"plug-and-play" cho các thành phần phần mềm** trên Windows. Nó cho phép một chương trình (ví dụ: Microsoft Word) có thể sử dụng chức năng của một chương trình khác (ví dụ: một trình kiểm tra ngữ pháp của bên thứ ba) mà không cần biết chi tiết mã nguồn của nhau.

COM là công nghệ nền tảng và được sử dụng rộng rãi trong toàn bộ hệ điều hành Windows, từ File Explorer, Internet Explorer cho đến các ứng dụng Office.

## 2. Các Thành Phần Cốt Lõi

Để hiểu cách COM hoạt động, cần nắm vững các thành phần chính sau:

| Thuật ngữ | Mô tả | Vai trò |
| :--- | :--- | :--- |
| **Object (Đối tượng)** | Một thành phần phần mềm cung cấp một hoặc nhiều dịch vụ. | Là đơn vị chức năng cơ bản. |
| **Interface (Giao diện)** | Một tập hợp các hàm (method) mà một đối tượng cung cấp. Giao diện hoạt động như một "hợp đồng" về những gì đối tượng có thể làm. | Cách duy nhất để tương tác với một đối tượng COM. |
| **CLSID (Class ID)** | Một **GUID** (Global Unique Identifier) 128-bit duy nhất, dùng để định danh một lớp (class) COM cụ thể. | Là "chứng minh nhân dân" của một lớp đối tượng. Mọi tra cứu đều bắt đầu từ đây. |
| **ProgID (Programmatic ID)** | Một tên định danh dễ đọc (ví dụ: `Excel.Application`) có thể được ánh xạ tới một CLSID. | Cung cấp một cách thân thiện hơn để tham chiếu đối tượng. |
| **COM Server** | Một tệp thực thi (`.dll` hoặc `.exe`) chứa mã nguồn để tạo và quản lý một hoặc nhiều đối tượng COM. | Là nơi chứa "bộ não" của đối tượng. |

---

## 3. Cách Windows Tìm và Tải một Đối Tượng COM

Đây là quy trình cốt lõi quyết định cách một đối tượng COM được kích hoạt. Hiểu rõ quy trình này là chìa khóa để hiểu các kỹ thuật tấn công liên quan.

1.  **Yêu cầu:** Một ứng dụng (Client) gọi một hàm API của Windows (ví dụ: `CoCreateInstance`) và cung cấp **CLSID** của đối tượng nó cần.

2.  **Tra cứu trong Registry:** Hệ điều hành Windows bắt đầu tìm kiếm CLSID đó trong Registry theo một **thứ tự ưu tiên nghiêm ngặt**:
    - **Đầu tiên:** `HKEY_CURRENT_USER\Software\Classes\CLSID\` **(HKCU)**
    - **Sau đó:** `HKEY_LOCAL_MACHINE\Software\Classes\CLSID\` **(HKLM)**

3.  **Xác định COM Server:** Khi tìm thấy CLSID, Windows sẽ đọc các khóa con bên trong để xác định vị trí của COM Server. Khóa quan trọng nhất là:
    - **`InProcServer32`**: Cho biết COM Server là một tệp DLL sẽ được tải **bên trong** tiến trình của ứng dụng yêu cầu (in-process). Giá trị của khóa này là đường dẫn tuyệt đối đến tệp DLL.
    - **`LocalServer32`**: Cho biết COM Server là một tệp EXE sẽ chạy trong một tiến trình riêng biệt (out-of-process).

4.  **Tải và Thực thi:**
    - Nếu là `InProcServer32`, Windows sẽ tải tệp DLL được chỉ định vào không gian bộ nhớ của ứng dụng yêu cầu và thực thi mã của nó.
    - Nếu là `LocalServer32`, Windows sẽ khởi chạy tệp EXE đó.

> **Điểm Mấu Chốt Về Bảo Mật:**
>
> Việc Windows **ưu tiên tra cứu trong `HKCU` trước `HKLM`** là cơ chế nền tảng cho phép kỹ thuật **COM Hijacking**. Một người dùng không có quyền quản trị vẫn có thể tạo khóa trong `HKCU` để "ghi đè" lên một đối tượng COM hệ thống được định nghĩa trong `HKLM`, vì đường dẫn của họ sẽ được tìm thấy và thực thi trước.

## 4. Tại Sao COM Quan Trọng với Red/Blue Team?

- **Đối với Red Team (Tấn công):**
    - **Bề mặt tấn công lớn:** COM được sử dụng ở khắp mọi nơi, tạo ra vô số cơ hội để khai thác.
    - **Persistence & Evasion:** Kỹ thuật COM Hijacking cho phép duy trì quyền truy cập và thực thi mã độc dưới vỏ bọc của các tiến trình hệ thống đáng tin cậy.

- **Đối với Blue Team (Phòng thủ):**
    - **Điểm giám sát quan trọng:** Việc giám sát các thay đổi trong Registry tại các đường dẫn `CLSID`, đặc biệt là dưới `HKCU`, là cực kỳ quan trọng để phát hiện các kỹ thuật persistence.
    - **Phân tích hành vi:** Hiểu rõ COM giúp các nhà phân tích nhận biết khi một tiến trình hợp pháp (như `explorer.exe`) đột nhiên tải một DLL từ một vị trí bất thường.