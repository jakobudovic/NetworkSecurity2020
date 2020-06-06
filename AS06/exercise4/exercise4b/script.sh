#!/bin/bash

ip link add dev wg1 type wireguard
# ip r add default via 172.21.152.1
ip route add 198.51.100.42 via 10.0.2.2 dev eth0         # rule 10
ip route add 10.0.0.0/8 via 10.0.2.2 dev eth0              # LAN network ranges
# ip address add dev wg1 10.90.84.0/24
ip a add dev wg1 10.90.84.2 peer 10.90.84.0/24

wg setconf wg1 /etc/wireguard/wg1.conf
ip link set up dev wg1
