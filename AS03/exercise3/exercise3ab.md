# Assignment 3

## Exercise 3a

[Overview of the host discovery commands](https://svn.nmap.org/nmap/docs/nmap.usage.txt)

Usage: nmap [Scan Type(s)] [Options] {target specification}

```
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
```

1. I checked what interfaces I have on my kali machine with `$ ip a` command. After seeing loopback, eth0 and eth1 i checked what ip corresponds to eth1 and used that for host discovery:

```console
kali@netsec-kali:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:97:50:3e brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute eth0
       valid_lft 63104sec preferred_lft 63104sec
    inet6 fe80::a00:27ff:fe97:503e/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:df:09:84 brd ff:ff:ff:ff:ff:ff
    inet 172.21.152.101/23 brd 172.21.153.255 scope global noprefixroute eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::fde9:7431:7092:d7f8/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

2. I then used the ip `172.21.152.101/23` to discover hosts
```console
kali@netsec-kali:~$ nmap -sn 172.21.152.101/23
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-06 15:45 CEST
Nmap scan report for 172.21.152.1
Host is up (0.00060s latency).
Nmap scan report for 172.21.152.44
Host is up (0.00051s latency).
Nmap scan report for 172.21.152.79
Host is up (0.00092s latency).
Nmap scan report for 172.21.152.101
Host is up (0.00051s latency).
Nmap scan report for 172.21.152.255
Host is up (0.0024s latency).
Nmap scan report for 172.21.153.10
Host is up (0.0026s latency).
Nmap scan report for 172.21.153.20
Host is up (0.00066s latency).
Nmap scan report for 172.21.153.135
Host is up (0.0023s latency).
Nmap done: 512 IP addresses (8 hosts up) scanned in 3.13 seconds
```

-sn flag means Ping scana aka disable port scan.

IPs 10, 20 and 135 above are all up because I got the reply back. 
1, 44, 79 and 101 are not available, 255 is broadcast.
```console
kali@netsec-kali:~$ ping 172.21.153.79
PING 172.21.153.79 (172.21.153.79) 56(84) bytes of data.
From 172.21.152.101 icmp_seq=1 Destination Host Unreachable
From 172.21.152.101 icmp_seq=2 Destination Host Unreachable
```

## Exercise 3b
Found them already.