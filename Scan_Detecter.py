from scapy.all import *
import os
Honey_ports = [1521, 3306, 22, 80, 443]
scan_count = 0
def detect_scan(packet):
    global scan_count
    if packet.haslayer(TCP) and packet.getlayer(TCP).flags == 2:
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        if dst_port in Honey_ports:
            scan_count += 1
            print(f"[!] ALERT #{scan_count}: STEALTH SCAN DETECTED!")
            print(f"    [+] Source IP: {src_ip}")
            print(f"    [+] Target: Port {dst_port}")
            print(f"    [Action] Logged to Security Database.\n")

sniff(filter="tcp", prn=detect_scan, store=0 , iface="lo0")
