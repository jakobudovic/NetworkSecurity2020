#!/usr/bin/env python3

# RECIEVING UDP
# source: https://wiki.python.org/moin/UdpCommunication

import socket

def handlestring(datastring, length, delimiter):
	stringlist = datastring.split(sep=delimiter)
	filteredlist = []
	for string in stringlist:
		filteredlist.append(string[length:])
	filteredstring = delimiter.join(filteredlist)
	return filteredstring


def main():
	s = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
	s.bind((host, port))
	# s.listen(backlog)

	while True:
		data, x = s.recvfrom(1024) # buffer size is 1024 bytes
		print("x:", x)
		datastring = data.decode("utf-8")
		# print("received message:", datastring)
		print(handlestring(datastring, len("spam "), "\n"))

if __name__ == "__main__":
	host = "localhost"
	port = 42424
	backlog = 5
	size = 1024
	main()

