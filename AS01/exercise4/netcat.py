#!/usr/bin/env python3

# SENDING UDP
# source: https://wiki.python.org/moin/UdpCommunication

import socket

host = "localhost"
port = 5005

# s = socket.create_connection((host, port))
s = socket.socket(socket.AF_INET, # Internet
					socket.SOCK_DGRAM) # UDP

for i in range(0,5):
	msg = "spam " + str(i) + "\n"
	# we are sending messages, still encoded, when we "make" them
	# previously, we've been storing them first in the buffer
	s.sendto(msg.encode("utf-8"), (host, port))

# we don't need to close socket here, since using UDP
# s.close()


