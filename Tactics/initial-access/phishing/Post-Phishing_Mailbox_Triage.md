# Post-Phishing: Mailbox Triage and Exfiltration

This procedure details the actions taken after an attacker gains credentials to a user's webmail account. The objective is to move from web-only access to full mailbox exfiltration and prepare for internal phishing.

---

### **Execution Flow**

1.  **Initial Access & Verification:** The attacker verifies the compromised credentials by logging into the webmail portal (e.g., on `http://<IP>:8181`).

2.  **Enumeration:** The attacker enumerates backend mail services to attempt exfiltration outside the restrictive web UI.
    *   **Port Scan (Nmap):** Scan the webmail host and related domains (e.g., `abc.xyz.vn`) for standard email protocol ports (`25, 110, 143, 465, 587, 993, 995`).
    *   **Interpret Results:**
        *   `open`: The port is accessible. Proceed to test credentials.
        *   `filtered`: A firewall is blocking access. Standard mail clients like Thunderbird will fail. The attacker must rely on the web UI or its APIs.
        *   `closed`: The port is accessible, but no service is running.

3.  **Bypassing Web UI Restrictions:** If standard mail ports are `filtered`, the attacker will use browser developer tools or a proxy like Burp Suite to analyze the webmail's HTTP traffic.
    *   Capture the authentication request (e.g., `POST /api/client-vmail/soap/authRequest`).
    *   Extract the API endpoint, required headers (`X-Gravitee-Api-Key`), and JSON body structure.
    *   Replay the request using a tool like `curl` to programmatically obtain an `authToken`.

4.  **Data Exfiltration:**
    *   **Method A (IMAP/POP3):** If ports are `open`, configure a mail client like Thunderbird or use command-line tools (`mutt`, `openssl s_client`) to connect and download all emails.
    *   **Method B (API):** Use the obtained `authToken` to make further API calls to list folders, retrieve messages, and download attachments.

5.  **Internal Pivoting (Phishing):** Using the context gained from reading the victim's emails (e.g., identifying them as "Trợ lý tác huấn, phòng đối ngoại"), the attacker uses the compromised account to send highly convincing spearphishing emails to other internal employees.

---

### **Detection Opportunities**

*   **Network:** Nmap scans from an external IP against mail infrastructure.
*   **Authentication Logs:**
    *   Anomalous logins to webmail or IMAP/SMTP from unexpected IP addresses, countries, or User-Agents.
    *   Multiple failed login attempts followed by a success.
*   **Mail Server Logs:** High-volume IMAP `FETCH` commands indicating a full mailbox download.

---

### **Mitigation Strategies**

*   **Multi-Factor Authentication (MFA):** Enforce MFA on all user-facing services, including webmail and especially on protocols like IMAP/SMTP.
*   **Network Segmentation:** Restrict direct internet access to IMAP/POP3/SMTP ports. Require users to be on a VPN to access these services, forcing all external access through the webmail portal (which should have MFA).
*   **API Rate Limiting & Monitoring:** Monitor API gateways for unusual activity or abuse of authentication tokens.```