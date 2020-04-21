#!/usr/bin/env python3

# RECIEVING UDP
# source: https://wiki.python.org/moin/UdpCommunication

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data.decode("utf-8"))
    print("received message:", data)

