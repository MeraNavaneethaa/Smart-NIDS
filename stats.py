from collections import Counter
import csv

def top_ips():

    ips = []

    try:
        with open("logs.csv", "r") as f:
            reader = csv.reader(f)

            for row in reader:
                ips.append(row[1])

    except:
        pass

    return Counter(ips).most_common(5)