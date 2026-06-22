import csv
from datetime import datetime

def log_event(ip, event, level):

    with open("logs.csv", "a", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            datetime.now(),
            ip,
            event,
            level
        ])