from sniffer import start_sniffing
from gui import show_logs
import threading

open("logs.csv", "w").close()

threading.Thread(
    target=start_sniffing,
    daemon=True
).start()

show_logs()