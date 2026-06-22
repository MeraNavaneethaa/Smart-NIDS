from scapy.all import sniff
from detector import analyze_packet

def process(packet):
    analyze_packet(packet)

def start_sniffing():

    print("Smart NIDS Started...")

    sniff(
        prn=process,
        store=0
    )