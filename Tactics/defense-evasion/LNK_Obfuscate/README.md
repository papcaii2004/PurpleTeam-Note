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

## Obfuscator

Rồi giờ thì ta có thể lợi dụng file LNK này như nào,

### Embed file VBS vào shortcut

### Embed Powershell vào shortcut

### Embed PE vào shortcut

## References

- **[Analysis & Simulation of Recent LNK Phishing](https://www.splunk.com/en_us/blog/security/lnk-phishing-analysis-simulation.html):**
- **[cybereason](https://www.cybereason.com/blog/threat-analysis-taking-shortcuts-using-lnk-files-for-initial-infection-and-persistence):**
- **[LNK file format abuse](https://blog.quarkslab.com/how-malware-authors-play-with-the-lnk-file-format.html#existing%20tools%20to%20analyze%20lnk%20files):**