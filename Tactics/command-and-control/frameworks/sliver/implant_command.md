# Sliver — Implant Commands (Reference Guide)

**Location:** `tactics/command_and_control/frameworks/sliver/implant_commands.md`

This guide summarizes essential commands for operating Sessions and Beacons in Sliver, focusing on efficiency, stealth, and common Red Team objectives.

---

## 1. Session Management & Context

Commands to manage implant state and determine current privileges.

| Command | Function | Red Team Focus |
| :--- | :--- | :--- |
| `use [ID]` | Switch active Session/Beacon context. | **First Step:** Required before interacting with the implant. |
| `info` | Display implant details (OS, C2, architecture). | Quick confirmation of target environment. |
| `whoami` | Get current user execution context. | Essential for Privilege Escalation assessment (T1078). |
| `getpid` | Get the implant process ID. | Needed for subsequent injection or evasion TTPs. |
| `reconfig` | Reconfigure Beacon check-in interval or C2. | Change timing parameters to avoid detection and maintain persistence. |
| **`interactive`** | Task a Beacon to switch to a real-time Session. | Transition from "low and slow" to direct exploitation (Beacon only). |
| `close` | Close interactive shell without killing the process. | Exit cleanly; preserve the implant's persistence. |
| `kill` | Terminate the remote implant process. | Use only for cleanup or replacement. |

---

## 2. Execution & Discovery

Commands for remote execution (T1059) and system enumeration (T1082).

| Command | Function | Red Team Optimization |
| :--- | :--- | :--- |
| **`execute`** | Execute a program remotely. | **Preference:** Better than `shell`; avoids spawning a new shell process, reducing detection risk. |
| `shell` | Start an interactive shell (`cmd`, `bash`). | Higher risk of detection; use when interactive scripting is necessary. |
| `execute-shellcode`| Execute given shellcode in the implant's process. | Run secondary payloads (e.g., Metasploit, C2s) entirely in memory. |
| `sideload` | Load and execute a shared library (.dll/.so) remotely. | Advanced Evasion: TTP for sophisticated process injection (T1574.002). |
| `ps` | List remote processes. | Identify targets for injection (`sideload`, `msf-inject`) or dumping (T1003). |
| `procdump` | Dump process memory. | Collect credentials or keys from memory (T1003). |
| `screenshot` | Take a remote screenshot. | Quick context gathering and proof of access. |

---

## 3. Filesystem & Evasion

Commands for file management and removing artifacts.

| Command | Function | Red Team Optimization |
| :--- | :--- | :--- |
| `upload` / `download` | Transfer files to/from the target. | Essential for staging tools and data Exfiltration (T1041). |
| `ls` / `cd` / `pwd` | Basic file navigation. | Find sensitive configuration files and user data (T1083). |
| `cat` | Dump file contents to console. | Quickly review sensitive files (e.g., config, logs). |
| **`chtimes`** | Change file access/modification times (Timestomp). | **Critical Evasion:** Alters timestamps to hide execution artifacts (T1070.006). |
| `rm` | Remove files or directories. | Clean up deployed tools and temporary logs. |

---

## 4. Networking & Pivoting

Commands for mapping the network and establishing pivot routes (T1210).

| Command | Function | Red Team Optimization |
| :--- | :--- | :--- |
| **`socks5`** | Start an In-band SOCKS5 Proxy. | **Primary Pivot:** Establishes a flexible tunneling route for lateral movement tools. |
| `portfwd` | In-band TCP Port Forwarding. | Route traffic from the victim host back to the C2 server. |
| `rportfwd` | Reverse Port Forwarding. | Tunnel traffic from the C2 server into the victim's network. |
| `netstat` | Print network connection information. | Discover open ports and connections on the host (T1049). |
| `ifconfig` | View network interface configuration. | Gather IP addresses and internal subnet information (T1016). |
| `ssh` | Run an SSH command on a remote host. | If implant host has SSH connectivity to other internal hosts. |