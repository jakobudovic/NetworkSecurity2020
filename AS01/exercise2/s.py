#!/usr/bin/env python3

# sending UDP
# source: https://wiki.python.org/moin/UdpCommunication

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode("utf-8"), (UDP_IP, UDP_PORT))
