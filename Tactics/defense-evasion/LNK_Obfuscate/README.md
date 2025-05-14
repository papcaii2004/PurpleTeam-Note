# LNK Obfuscator

> Chà .lnk nghe lạ phải không, nhưng thực ra lại khá quen thuộc đấy. Nó y như mấy file shortcut mà ta thường dùng. Và chính nó lại là một yếu tố mà các hacker dựa vào để lợi dùng, nhưng, lợi dụng như nào ?

## Overview

### File .LNK là gì ?

- Theo Windows, đây là một file format được gọi là `Shell Link (.LNK)`, hay có thể gọi là shortcut.
- Những file này có thể chứa những thông tin được dùng để truy cập một file/object khác, có thể là:
	- Mở một trang web trong browser
	- Mở một thư mục
	- Hay... Chạy ngầm một mã độc !

### Structure của file LNK

File LNK gồm 4 cấu trúc chính:

**1. Shell Link Header** 
	- Chứa Signature, LinkFlags,
**2. LinkTargetIDList** - Mô tả các ID xác định target của shortcut
**3. LinkInfo** - Cung cấp thông tin về Link
**4. ExtraData** - Chứa các data bổ sung như `STRING_DATA`, `TrackerDataBlock`, v.v.

## 