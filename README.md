# Security Operations: Regex Log Parser

## 📝 Description
This security utility is written in Python to automate log analysis for Security Operations Center (SOC) environments. It reads raw server access/authentication logs (`server.log`) and uses Regular Expressions (Regex) to parse, identify, and count brute-force attack signatures or failed SSH/web login attempts.

## 🛠️ Features
* **Automated Log Parsing:** Avoids manual analysis by filtering text streams using Python's native `re` library.
* **Attack Counter:** Aggregates data using `collections.Counter` to track frequencies of offending IPs.
* **Incident Highlights:** Instantly alerts analysts to high-frequency suspicious activity.

## 🚀 How to Run It

### Prerequisites
* Python 3.x installed.

### Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/regex-log-parser.git](https://github.com/YOUR-USERNAME/regex-log-parser.git)
