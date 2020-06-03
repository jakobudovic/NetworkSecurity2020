#!/bin/bash
ip link add dev wg0 type wireguard
# ip address add dev wg0 10.90.42.2/24
ip address add dev wg0 10.90.42.2 peer 10.90.42.0/24
wg setconf wg0 myconfig1.conf

ip link set up dev wg0
