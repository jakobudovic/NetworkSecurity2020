#!/usr/bin/env python3

import socket
import struct
import sys

def int_to_mac(macint):
	# source: https://gist.github.com/nlm/9ec20c78c4881cf23ed132ae59570340
    if type(macint) != int:
        raise ValueError('invalid integer')
    return ':'.join(['{}{}'.format(a, b)
                     for a, b
                     in zip(*[iter('{:012x}'.format(macint))]*2)])

def parse_ethernet(packet):
	header = packet[:20]
	

	# see notes to know the meaning behind variables; eda - eth. dest. address
	eda, ed, es, esa, tag1, tag2, typ, _ =  struct.unpack("!LHHLHHHH", header)
	
	typeCode = tag1
	if tag1 == 0x81 and tag2 == 0x00:
		typeCode = typ # present tag, read from bytes 17 and 18
		data = packet[18:]
	else:
		data = packet[12:]

	macD = int_to_mac(int(str(eda) + str(ed)))
	macS = int_to_mac(int(str(es) + str(esa)))

	# print("macD:", macD)
	# print("macS:", macS)

	return macD, macS, typeCode, data


def parse_ip(packet):
	header_length_in_bytes = (packet[0] & 0x0F) * 4 # 0x0F == 00001111
	header = packet[:header_length_in_bytes]
	data = packet[header_length_in_bytes:]

	_, totalLength, _, _, protocol, _, source, destination  = struct.unpack_from("!HHLBBH4s4s", header, offset=0)
	# print("protocol: ", protocol)
	sourceIP = socket.inet_ntoa(source)
	destIP = socket.inet_ntoa(destination)	

	return header_length_in_bytes, totalLength, protocol, sourceIP, destIP, data


def parse_udp(packet):
	header_length = 8
	header = packet[:header_length]
	data = packet[header_length:]
	
	(source_port, dest_port, data_length, checksum) = struct.unpack("!HHHH", header)
	return source_port, dest_port, data_length, checksum, data

def main():
	s = socket.socket(family=socket.AF_PACKET, 
						type=socket.SOCK_RAW, 
						proto=socket.ntohs(0x0003))	# protocol
	
	while True:
		data, addr = s.recvfrom(size) # data and addres of sending socketport
		
		ethDest, ethSource, ethType, dataFromETH = parse_ethernet(data)

		if ethType != 0x800:	# check if it's an IP type code, skip if it's not
			print("Not an IP data, ethType:", hex(ethType))
			continue
		else: 
			print("IP data")
			# print(dataFromETH, "\n")

		headerLenIP, totalLength, protocol, sourceIP, destinationIP, dataFromIP = parse_ip(dataFromETH)
		
		# check if it's a UDP protocol packet, 17
		if protocol != 17:
			print("Not an UDP packet, protocol:", protocol)
			# print(dataFromIP, "\n")
			# continue
		else: 
			print("UDP packet ----------------------------------------- !!!")
		
		sourcePort, destPort, dataLen, checksum, dataFromUDP = parse_udp(dataFromIP)
		# print(dataFromUDP, "\n")
		

		print("Ethernet source: {}\nEthernet destination: {}\n"
				"IP header length: {}\nIP total length: {}\n"
				"IP protocol: {}\nIP source: {}\n"
				"IP destination: {}\n"
				"UDP source port: {}\nUDP destination port: {}\n"
				"UDP payload length: {}\n\nData: {}\n".format(
				ethSource, ethDest, headerLenIP, totalLength, 
				protocol, sourceIP, destinationIP, 
				sourcePort, destPort, dataLen, struct.unpack('f', dataFromUDP)))
		

if __name__ == "__main__":
	host = "localhost"
	# port = 42424
	port = 5005
	backlog = 5
	size = 65565
	main()