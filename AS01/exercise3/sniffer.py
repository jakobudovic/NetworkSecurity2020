#!/usr/bin/env python3

import socket
import struct
import sys

def parse_ip(packet):
	header_length_in_bytes = (packet[0] & 0x0F) * 4 # 0x0F == 00001111
	header = packet[:header_length_in_bytes]

	# structs: https://docs.python.org/3.6/library/struct.html#module-struct
	_, totalLength, _, _, protocol, _, source, destination  = struct.unpack_from("!HHLBBH4s4s", header, offset=0)
	sourceIP = socket.inet_ntoa(source)
	destIP = socket.inet_ntoa(destination)

	""" somehow weird result form. This is a "former" attempt. I rather used "latter" (see above)
	totalLength = struct.unpack("!H", header[2:4])
	protocol = struct.unpack("!B", header[9:10])
	sourceAdd = struct.unpack("!I", header[12:16])
	destinationAdd = struct.unpack("!I", header[16:20])
	"""

	data = packet[header_length_in_bytes:]

	return totalLength, protocol, sourceIP, destIP, data


def parse_udp(packet):
	header_length = 8
	header = packet[:header_length]
	data = packet[header_length:]
	
	# structs: https://docs.python.org/3.6/library/struct.html#format-strings
	(source_port, dest_port, data_length, checksum) = struct.unpack("!HHHH", header)
	return source_port, dest_port, data_length, checksum, data

def main():
	s = socket.socket(family=socket.AF_INET, 
						type=socket.SOCK_RAW, 
						proto=socket.IPPROTO_UDP)	# protocol
	# s.setsockopt(Wsocket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	while True:
		data, addr = s.recvfrom(size) # data and addres of sending socket
		# print(s.recvfrom(size))

		totalLength, protocol, sourceIP, destinationIP, dataFromIP = parse_ip(data)
		source_port, dest_port, data_length, checksum, dataFromUDP = parse_udp(dataFromIP)

		print("===============================================================================\n")
		
		print("IP:")
		print("totalLength IP: {}\nprotocol: {}\n"
				"sourceIP: {}\ndestinationIP: {}\n".format(
				totalLength, protocol, sourceIP, destinationIP))
		print("dataFromIP: ", dataFromIP, "\n")
		
		print("------------")
		
		print("UDP:")
		print("Source Port: {}\nDestination Port: {}\n"
				"Data length: {}\nChecksum: {}\n".format(
				source_port, dest_port, data_length, checksum))
		print("dataFromUDP: ", dataFromUDP)

		print("===============================================================================\n\n")


if __name__ == "__main__":
	host = "localhost"
	port = 42424
	backlog = 5
	size = 65565
	main()