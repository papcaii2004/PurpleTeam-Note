# T1566.001 - Spearphishing Attachment: RAR Path Traversal

This procedure tests defenses against a phishing lure using a path traversal vulnerability (e.g., CVE-2023-38831) in archive utilities. The goal is to gain initial access and persistence by dropping a payload into the user's Startup folder.

---

### **Execution Flow**

1.  **Resource Development:** The Red Team crafts a malicious RAR archive using the [Python exploit builder](./Payloads/CVE-2025-8088-RAR-Path-Traversal-Builder/final_exploit_builder.py).
    *   The script uses a legitimate document (e.g., PDF, DOCX) as a visual decoy.
    *   A secondary, low-profile text file (`metadata.txt`) is created to act as a carrier.
    *   Multiple Alternate Data Streams (ADS), each containing the payload and a unique path traversal string (`../`, `../../`, etc.), are attached to `metadata.txt`.
    *   Both the decoy and the weaponized carrier are packaged into a single RAR file.
2.  **Initial Access:** A targeted spearphishing email with the malicious RAR file attached is sent to the victim.
3.  **Execution & Persistence:** The victim extracts the archive. The vulnerable archiver processes the ADS from the carrier file, causing the payload (`payload.bat`) to be written to the user's Startup folder. The payload executes on the next user login.

---

### **Detection Opportunities**

*   **Email Gateway:** Detection of `.rar` attachments; YARA rules looking for RAR5 headers with multiple `STM` (NTFS Stream) service headers.
*   **Endpoint (EDR):**
    *   **High-Fidelity:** An archive utility process (`WinRAR.exe`) writing a file to a location outside of the designated extraction path, especially the Startup folder.
    *   **High-Fidelity:** Creation of a new executable (`.bat`, `.ps1`, `.exe`) in any user's Startup folder.
    *   **Investigative:** Filesystem monitoring for the creation of files with multiple Alternate Data Streams (e.g., via `Get-Item -Stream *`).

---

### **Mitigation Strategies**

*   **Patch Management:** Ensure all archive utilities (WinRAR, 7-Zip, etc.) are kept fully patched.
*   **Email Attachment Filtering:** Block or quarantine `.rar` and other risky archive formats at the email gateway.
*   **Application Control:** Use AppLocker or WDAC to prevent unauthorized scripts from running from user-writable locations like the Startup folder.

---

### **Tooling**

*   The exploit builder script is located at: `Tactics/initial-access/phishing/Payloads/CVE-XXXX-RAR-Path-Traversal-Builder/`