#!/bin/bash

ip link add dev wg0 type wireguard
ip address add dev wg0 10.90.42.2/24 dev wg0
ip address add dev wg0 10.90.42.2 peer 10.90.42.0/24
ip address add dev eth1 172.21.152.101 peer 10.90.42.2
wg setconf wg0 /etc/wireguard/wg0.conf
# wg set wg0 private-key 
ip link set up dev wg0
