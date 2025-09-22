# Email Protocols: SMTP, POP3, and IMAP

This document outlines the three core protocols used for sending and receiving email. Understanding their roles is critical for both offensive and defensive operations.

---

### **1. SMTP (Simple Mail Transfer Protocol)**
- **Function:** **Sending email**. It handles the transfer of email from a client to a server, and between mail servers.
- **Role:** The "post office" that sends mail out.
- **Default Ports:**
  - `25`: Server-to-server communication.
  - `587` (Submission with STARTTLS): Modern standard for client-to-server sending.
  - `465` (SMTPS): Older standard using SSL/TLS from the start.
- **Mnemonic:** **S**MTP = **S**end **M**ail.

---

### **2. POP3 (Post Office Protocol v3)**
- **Function:** **Receiving email**. It is designed to download emails from a server to a local client.
- **How it works:** Typically downloads all emails from the inbox and then **deletes them from the server**. (This behavior can be changed by a "leave a copy on the server" setting).
- **Default Ports:**
  - `110`: Unencrypted.
  - `995` (POP3S): Encrypted with SSL/TLS.
- **Use Case:** Best for single-device access where a permanent offline copy is desired. Poor for multi-device sync.
- **Mnemonic:** **P**OP3 = **P**ulls mail (and often deletes).

---

### **3. IMAP (Internet Message Access Protocol)**
- **Function:** **Receiving and managing email**. It is the modern standard for multi-device access.
- **How it works:** Keeps all emails and folder structures **on the server**. The client syncs with the server, reflecting all changes (read, delete, move) across all connected devices.
- **Default Ports:**
  - `143`: Unencrypted (often uses STARTTLS to upgrade).
  - `993` (IMAPS): Encrypted with SSL/TLS from the start.
- **Use Case:** Standard for webmail (Gmail, O365) and any user who accesses email from a phone, laptop, and desktop.
- **Mnemonic:** **I**MAP = **I**nteractive **M**ail (syncs everywhere).