# AV Mechanism

> Note này phân tích các cơ chế hoạt động cốt lõi của Anti-Virus, tập trung vào Phân tích Tĩnh và Phân tích Động, nhằm cung cấp kiến thức nền tảng cho Red Team trong việc phát triển và triển khai các kỹ thuật bypass.

## I. Giới thiệu

Anti-Virus (AV) là tuyến phòng thủ quan trọng, nhưng không phải là bất khả xâm phạm. Hiểu rõ cách AV hoạt động là bước đầu tiên để xây dựng các payload và chiến thuật có khả năng vượt qua chúng. AV hiện đại sử dụng nhiều lớp phát hiện, nhưng có thể quy về hai phương pháp chính: Phân tích Tĩnh và Phân tích Động.

---

## II. Phân Tích Tĩnh (Static Analysis)

Phân tích tĩnh kiểm tra một tệp tin mà không cần thực thi nó. AV sẽ phân tích cấu trúc, nội dung và các đặc điểm khác của tệp để tìm dấu hiệu độc hại.

### 1. Phát hiện dựa trên Chữ ký (Signature-based Detection)

- **Cách AV làm:** AV duy trì một cơ sở dữ liệu lớn các "chữ ký" – là các chuỗi byte hoặc hash (MD5, SHA1, SHA256, fuzzy hash như ssdeep) duy nhất được trích xuất từ các mẫu malware đã biết. Khi quét, AV so sánh các phần của tệp hoặc hash của tệp với cơ sở dữ liệu này.  
- **Điểm mạnh (cho AV):** Nhanh, chính xác cao với malware đã biết, ít dương tính giả.

### 2. Phân tích Heuristic Tĩnh (Static Heuristics)

- **Cách AV làm:** AV không chỉ tìm một đặc điểm đơn lẻ mà thường đánh giá **tổng hợp nhiều yếu tố** và **các chuỗi hành vi tiềm năng** dựa trên phân tích tĩnh.
  - **Gán điểm (Scoring):** Mỗi đặc điểm "đáng ngờ" được phát hiện có thể được gán một số điểm nhất định.
    - Sử dụng API nguy hiểm như `VirtualAlloc` với quyền `PAGE_EXECUTE_READWRITE`: +10 điểm
    - Gọi `WriteProcessMemory` sau `VirtualAlloc`: +8 điểm
    - Gọi `CreateRemoteThread` trỏ đến vùng nhớ đã cấp phát: +15 điểm
    - Dùng `SetWindowsHookEx` để hook toàn cục: +12 điểm
    - Entropy cao trong section: +5 điểm
    - Chuỗi đáng ngờ: +3 điểm mỗi chuỗi
    - PE header bất thường: +2 đến +7 điểm
    - Packer/crypter đã biết: +5 điểm
    - Anti-debug / anti-VM: +4 điểm
  - **Ngưỡng phát hiện:**
    - "Đáng ngờ": 20 điểm  
    - "Độc hại": 35 điểm
  - **Chuỗi hành vi tiềm năng:**
    - `VirtualAlloc` + `WriteProcessMemory` + `CreateRemoteThread`
    - File nhỏ, entropy cao, gọi hàm giải mã và thực thi mã

### 3. Phân tích Cấu trúc Tệp (File Structure Analysis)

- **Cách AV làm:** Kiểm tra định dạng tệp chuẩn (PE, ELF, PDF...), phát hiện các bất thường.

### 4. Phân tích String và Import/Export Table

- **Cách AV làm:** Trích xuất và phân tích chuỗi văn bản và danh sách hàm import/export.

### 5. Yara Rule Detection

- **Cách AV làm:** Sử dụng Yara rule để phát hiện mã độc dựa trên pattern matching.
- **Ví dụ:**

```yara
rule ExampleMalware
{
    strings:
        $s1 = "This program cannot be run in DOS mode"
        $s2 = { E8 ?? ?? ?? ?? 83 C4 04 C3 }
    condition:
        all of them
}
```

- **Điểm mạnh:** Dễ tùy biến, mạnh trong nhận diện biến thể.

---

## III. Phân Tích Động (Dynamic Analysis)

Phân tích động liên quan đến việc thực thi mã trong môi trường kiểm soát (sandbox, emulator...) để quan sát hành vi thực tế.

### 1. Sandboxing và Emulation

- **Cách AV làm:**
  - Gán điểm cho các hành vi nguy hiểm khi mã chạy trong môi trường mô phỏng.
  - Phát hiện chuỗi hành vi phức tạp.
- **Ví dụ chuỗi có điểm cao:**
  - `WriteProcessMemory` → `CreateRemoteThread` → chạy shellcode
  - Kết nối C2 → tải payload → thực thi
  - Mã hóa hàng loạt tệp (ransomware)
- **Sandbox AV phổ biến:**
  - [Cuckoo Sandbox](https://cuckoosandbox.org) – mã nguồn mở
  - Joe Sandbox – thương mại, đa nền tảng
  - Microsoft Defender ATP Sandbox – tích hợp trong Windows 10/11 và EDR

### 2. Giám sát Hành vi (Behavioral Monitoring / Runtime Protection)

- **Cách AV làm:**
  - Theo dõi thời gian thực hoạt động của tiến trình.
  - Áp dụng rule hoặc IOC để xác định hành vi đáng ngờ.
- **Ví dụ chuỗi hành vi:**
  - Process lạ → WMI persistence → network call → download & exec

### 3. API Hooking

**Hooking là kỹ thuật chèn mã vào quá trình thực thi của chương trình nhằm kiểm soát hoặc giám sát hành vi.** AV/EDR sử dụng API hooking để phát hiện và can thiệp vào các hành vi đáng ngờ ở cả hai cấp độ: **User Mode** và **Kernel Mode**.

#### a. User-mode API Hooking

* **Cách làm:**

  * Hook trực tiếp vào các hàm trong userland DLL như `kernel32.dll`, `ntdll.dll`, `user32.dll`, ...
  * Phổ biến các dạng:

    * **Inline Hooking:** Ghi đè byte đầu của API bằng mã nhảy (`jmp`) đến hàm giám sát.
    * **IAT Hooking (Import Address Table):** Thay đổi con trỏ hàm trong bảng import để chuyển hướng tới hàm hook.
    * **EAT Hooking (Export Address Table):** Sử dụng với DLL bị nạp động (`LoadLibrary`, `GetProcAddress`).
* **Mục tiêu thường bị hook:**

  * `CreateProcess`, `VirtualAlloc`, `WriteProcessMemory`, `CreateRemoteThread`, `NtOpenProcess`, `LoadLibrary`, ...
* **Ưu điểm:** Dễ triển khai, quan sát chi tiết API gọi và tham số.
* **Nhược điểm:**

  * Có thể **bị bypass** thông qua:

    * Gọi syscall trực tiếp (`syscall stub`) để né qua `ntdll.dll`.
    * Manual Mapping DLL để tránh bảng IAT.
    * Inline shellcode không dùng API.

#### b. Kernel-mode API Hooking

* **Cách làm:** Hook các hàm trong kernel như `Nt*` hoặc `Zw*` tại tầng SSDT (System Service Dispatch Table), hoặc IRP hooks với driver.
* **Hook SSDT:**

  * AV cài driver kernel hook vào SSDT entry, chuyển hướng các syscall quan trọng đến handler riêng.
  * Ví dụ: hook `NtCreateProcess`, `NtMapViewOfSection`, `NtProtectVirtualMemory`.
* **IRP Hooking (I/O Request Packet):**

  * Hook xử lý IRP của thiết bị để chặn hành vi như ghi file, registry, network,...
* **Ưu điểm:** Khó bypass hơn, giám sát ở tầng thấp, khó bị phát hiện hoặc can thiệp từ userland.
* **Nhược điểm:**

  * Dễ gây **xung đột hệ thống** nếu hook sai.
  * Có thể bị **bypass** bởi:

    * Driver chưa bị giám sát (signed malware driver).
    * Kỹ thuật như **DKOM** (Direct Kernel Object Manipulation).
    * Bootkit, rootkit phá vòng kiểm tra integrity.

---

**Tóm lại:**

| Mức độ      | Hook vị trí                               | Ưu điểm                            | Nhược điểm                          |
| ----------- | ----------------------------------------- | ---------------------------------- | ----------------------------------- |
| User-mode   | `kernel32.dll`, `ntdll.dll` (IAT, inline) | Dễ triển khai, quan sát rõ hành vi | Bypass dễ với syscall/direct access |
| Kernel-mode | SSDT, IRP, Object Callback                | Quan sát ở tầng thấp, mạnh hơn     | Phức tạp, dễ gây crash nếu lỗi      |

---
