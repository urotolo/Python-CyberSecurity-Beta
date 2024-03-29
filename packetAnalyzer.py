#!/usr/bin/py
# This code prints Source and Destination IP from the given 'pcap' file

import dpkt
import socket


def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            # read the source IP in src
            src = socket.inet_ntoa(ip.src)
            # read the destination IP in dst
            dst = socket.inet_ntoa(ip.dist)

            # Print the source and destination IP
            print 'Source: ' +src+ ' Destination: ' +dst

        except:
            pass
def main():
    # Open pcap file for reading
    f = open('/root/Documents/capturedWifiPackets.pcap')
    # Pass the file argument to the pcap.Reader function
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)

if __name__ == '__main__':
    main()


