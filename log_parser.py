import re
from collections import Counter

log_file_path = "server.log"
failed_pattern = r"FAILED:.*from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
failed_ips = []

print("-" * 50)
print("🛡️ SEC OPS LOG PARSER DETECTING ATTACKS... 🛡️")
print("-" * 50)

with open(log_file_path, "r") as file:
    for line in file:
        match = re.search(failed_pattern, line)
        if match:
            ip_address = match.group(1)
            failed_ips.append(ip_address)

ip_counts = Counter(failed_ips)

if ip_counts:
    print(f"[!] ALERT: Found {len(failed_ips)} failed login attempts!")
    print("\nSuspicious IP Address Brute-Force Counts:")
    for ip, count in ip_counts.items():
        print(f"👉 IP: {ip:15} | Failed Attempts: {count}")
else:
    print("[+] No failed login alerts found in logs.")

print("-" * 50)
