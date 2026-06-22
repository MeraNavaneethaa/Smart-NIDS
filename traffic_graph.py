import csv
import matplotlib.pyplot as plt
from collections import Counter

ips = []

try:
    with open("logs.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) >= 4:
                ips.append(row[1])

except:
    print("No logs found.")
    exit()

top_ips = Counter(ips).most_common(5)

ip_names = []
counts = []

for ip, count in top_ips:
    ip_names.append(ip)
    counts.append(count)

plt.figure(figsize=(8,5))

plt.bar(ip_names, counts)

plt.title("Top Suspicious IPs")
plt.xlabel("IP Address")
plt.ylabel("Alert Count")

plt.xticks(rotation=15)

plt.tight_layout()

plt.show()