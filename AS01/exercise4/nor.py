#!/usr/bin/env python3

import socket
import struct 
import ipaddress

def convertMAC(byteMAC):
    result =""

    byteMAC = list(byteMAC)
    
    for byte in byteMAC:

        second = byte & 0x0F
        first = (byte>>4) & 0x0F
        
        first = hex(first).lstrip("0x")
        second = hex(second).lstrip("0x")

        if first == '':
            first = '0'
        if second =='':
            second = '0'        
        result= result + first + second + "::"

    result = result[:len(result)-2]
    return result        



def parse_ethernet(packet):
    packet= packet[0]
    eth_dest_addr = packet[:6]
    eth_source_addr = packet[6:12]

    payload = b''
    type_code =b''
    #type code is the length of the payload == ip datagram
    if packet[12:16] == b'\x81\x00':
        type_code = packet[16:18]
        length = int.from_bytes(type_code,byteorder='big')
        payload = packet[16:length]
    else:
        type_code = packet[12:14]
        length = int.from_bytes(type_code,byteorder='big')
        payload = packet[14:length]

    return eth_dest_addr, eth_source_addr,type_code, payload
    

def parse_ip(packet):
    #packet= packet[0]
    header_length_in_bytes = (packet[0]& 0x0F) *4 
    header = packet[: header_length_in_bytes]
    (version_and_IHL, type_of_service, total_length, 
    identification, flags_and_fragment_offset, ttl, protocol, header_cksum, source_addr, dest_addr)=struct.unpack_from("!BBHHHBBHII", header)
    data = packet[header_length_in_bytes:]

    dotted_source_ip = ipaddress.IPv4Address(source_addr)
    dotted_destination_ip = ipaddress.IPv4Address(dest_addr)

    return header_length_in_bytes, (total_length, protocol, dotted_source_ip, dotted_destination_ip), data 

def parse_udp(packet):

    header_length = 8
    header = packet[:header_length]
    data = packet[header_length:]
    (source_port, dest_port,data_length, checksum) = struct.unpack("!HHHH", header)
    
    print("Source Port: {}\nDestination Port: {}\n"
            "Data length: {}\nChecksum: {}\nData: {}\nActual Data length: {}\n".format(source_port,dest_port,data_length,checksum,data,len(data)))
    return source_port, dest_port, data_length, checksum, data 

def main():
    s= socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x003))

    while True:

        (e_dest, e_source, type_code, payload) = parse_ethernet(s.recvfrom(65565))
        print("Ethernet info:",(convertMAC(e_dest),convertMAC(e_source), type_code) )

        if type_code == b'\x08\x00':
            
            (header_len, header, data) = parse_ip (payload) 
            print("Internet info:",header_len, header)
            (total_length, protocol, dotted_source_ip, dotted_destination_ip)= header
            
            if protocol== 17:
                print("Transport info + data:")
                parse_udp(data)



if __name__ == "__main__":
        
    host = "localhost"
    port = 42424
    backlog = 5 
    size = 1024

main()

