from logger import log_event
import time

ip_counter = {}
last_alert_time = {}

ALERT_COOLDOWN = 10

def analyze_packet(packet):

    if packet.haslayer("IP"):

        src = packet["IP"].src

        ip_counter[src] = ip_counter.get(src, 0) + 1

        count = ip_counter[src]

        # Ignore small traffic
        if count < 20:
            return

        # Warning traffic
        elif count < 40:

            now = time.time()

            if src not in last_alert_time or (now - last_alert_time[src]) > ALERT_COOLDOWN:

                log_event(
                    src,
                    "Traffic Spike Detected",
                    "WARNING"
                )

                last_alert_time[src] = now

        # Critical traffic
        else:

            now = time.time()

            if src not in last_alert_time or (now - last_alert_time[src]) > ALERT_COOLDOWN:

                log_event(
                    src,
                    "Possible Scan / DoS Attack",
                    "CRITICAL"
                )

                print("⚠ ALERT:", src)

                with open("blacklist.txt", "a") as f:
                    f.write(src + "\n")

                last_alert_time[src] = now