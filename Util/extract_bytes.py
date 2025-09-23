#!/usr/bin/env python3
"""
Trích xuất toàn bộ byte từ một file nhị phân (ví dụ: .exe)
và sinh ra một file Python chứa biến payload = b"\\xYY\\xYY..."
(dạng Hex tuyệt đối, không bị chuyển thành ký tự ASCII)
"""

import os

# ==== Tùy chỉnh ====
input_file  = "abc.lnk"          # File cần trích xuất
output_file = "output_bytes.py"      # File Python đầu ra
chunk_size  = 1024                   # Số byte xử lý mỗi lần

def bytes_to_hex_literal(b: bytes) -> str:
    # Chuyển từng byte thành \xYY
    return ''.join(f'\\x{byte:02x}' for byte in b)

def main():
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Không tìm thấy file: {input_file}")

    with open(input_file, "rb") as src, open(output_file, "w", encoding="utf-8") as dst:
        dst.write("# Auto-generated payload file\n")
        dst.write("payload = b''\n")
        while chunk := src.read(chunk_size):
            hex_chunk = bytes_to_hex_literal(chunk)
            dst.write(f"payload += b\"{hex_chunk}\"\n")

    print(f"[+] Đã trích xuất {os.path.getsize(input_file)} bytes")
    print(f"[+] File Python đã tạo: {output_file}")

if __name__ == "__main__":
    main()
