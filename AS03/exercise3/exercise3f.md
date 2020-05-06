# Assignment 3

## Exercise 3f

### OS Fingerprinting
[1:42:00 Lecture3 - OS Fingerprinting](https://youtu.be/Xhm-NWz8kVY?t=6122)

For version detection we use `-sV` and forthe operating system: `-O`

**`-A`**: Enable OS detection, version detection, script scanning, and traceroute.

I could also use `netstat` for serivce seek with `ss -tl`  
**`ss -tln`** - numeric output  
**`ss -tlnp`** - processing output

[1:26:00 Lecture 3 - version detection and services with netstsat (ss)](https://youtu.be/Xhm-NWz8kVY?t=5158) 
```dos
foo@bar:~$ whoami
foo
```


```console
kali@netsec-kali:~$ sudo nmap -p 1-65535 -A 172.21.152.101/23
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-06 16:57 CEST
Nmap scan report for 172.21.152.1
Host is up (0.00059s latency).
Not shown: 65529 closed ports
PORT    STATE    SERVICE VERSION
21/tcp  open     ftp     Pure-FTPd
22/tcp  open     ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 bb:43:8f:bc:bd:5d:39:22:43:10:ca:9a:59:ab:8f:be (RSA)
|   256 10:d2:b0:59:79:cf:fd:58:4b:98:d9:6c:46:ea:3e:16 (ECDSA)
|_  256 0c:71:d9:f3:21:4c:f2:b2:8a:9b:2b:14:96:ce:2d:1f (ED25519)
80/tcp  open     http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Welcome to nginx!
512/tcp filtered exec
513/tcp filtered login
514/tcp filtered shell
MAC Address: 08:00:27:AB:03:CB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=21%CT=1%CU=43256%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=5EB2D17E%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=103%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O5
OS:=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.59 ms 172.21.152.1

Nmap scan report for 172.21.152.44
Host is up (0.00049s latency).
Not shown: 65534 closed ports
PORT   STATE SERVICE VERSION
25/tcp open  smtp    Postfix smtpd
|_smtp-commands: netsec-peer1.octopus.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING, 
| ssl-cert: Subject: commonName=netsec-peer1
| Subject Alternative Name: DNS:netsec-peer1
| Not valid before: 2020-05-04T08:01:37
|_Not valid after:  2030-05-02T08:01:37
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=25%CT=1%CU=31593%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=5EB2D17E%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O5
OS:=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Network Distance: 1 hop
Service Info: Host:  netsec-peer1.octopus.localdomain

TRACEROUTE
HOP RTT     ADDRESS
1   0.49 ms 172.21.152.44

Nmap scan report for 172.21.152.79
Host is up (0.00057s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE         VERSION
79/tcp   open  finger?
| finger: 
| Debian GNU/Linux      Copyright (c) 1993-1999 Software in the Public Interest
| 
|                  Your site has been rejected for some reason.
| 
|          This may be caused by a missing RFC 1413 identd on your site.
| 
|                  Contact your and/or our system administrator.
|_
| fingerprint-strings: 
|   SIPOptions: 
|     Debian GNU/Linux Copyright (c) 1993-1999 Software in the Public Interest
|     Your site has been rejected for some reason.
|     This may be caused by a missing RFC 1413 identd on your site.
|_    Contact your and/or our system administrator.
443/tcp  open  ssh             OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 bb:43:8f:bc:bd:5d:39:22:43:10:ca:9a:59:ab:8f:be (RSA)
|   256 10:d2:b0:59:79:cf:fd:58:4b:98:d9:6c:46:ea:3e:16 (ECDSA)
|_  256 0c:71:d9:f3:21:4c:f2:b2:8a:9b:2b:14:96:ce:2d:1f (ED25519)
4242/tcp open  vrml-multi-use?
9100/tcp open  jetdirect?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port79-TCP:V=7.80%I=7%D=5/6%Time=5EB2D0DF%P=x86_64-pc-linux-gnu%r(SIPOp
SF:tions,117,"\nDebian\x20GNU/Linux\x20\x20\x20\x20\x20\x20Copyright\x20\(
SF:c\)\x201993-1999\x20Software\x20in\x20the\x20Public\x20Interest\n\n\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20Your\x2
SF:0site\x20has\x20been\x20rejected\x20for\x20some\x20reason\.\n\n\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20This\x20may\x20be\x20caused\x20by\x20a\x20m
SF:issing\x20RFC\x201413\x20identd\x20on\x20your\x20site\.\n\n\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20Contact\x20your
SF:\x20and/or\x20our\x20system\x20administrator\.\n\n");
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=79%CT=1%CU=43174%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=5EB2D17E%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10C%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O5
OS:=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.57 ms 172.21.152.79

Nmap scan report for 172.21.152.255
Host is up (0.00057s latency).
All 65535 scanned ports on 172.21.152.255 are closed
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.57 ms 172.21.152.255

Nmap scan report for 172.21.153.10
Host is up (0.00054s latency).
Not shown: 65533 closed ports
PORT      STATE SERVICE VERSION
16765/tcp open  http    lighttpd 1.4.53
|_http-server-header: lighttpd/1.4.53
|_http-title: Welcome page
22222/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 bb:43:8f:bc:bd:5d:39:22:43:10:ca:9a:59:ab:8f:be (RSA)
|   256 10:d2:b0:59:79:cf:fd:58:4b:98:d9:6c:46:ea:3e:16 (ECDSA)
|_  256 0c:71:d9:f3:21:4c:f2:b2:8a:9b:2b:14:96:ce:2d:1f (ED25519)
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=16765%CT=1%CU=40452%PV=Y%DS=1%DC=D%G=Y%M=080027
OS:%TM=5EB2D1BF%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=107%TI=Z%CI=Z%II
OS:=I%TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4
OS:%O5=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%
OS:W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S
OS:=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%R
OS:D=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=
OS:0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U
OS:1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DF
OS:I=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.54 ms 172.21.153.10

Nmap scan report for 172.21.153.20
Host is up (0.00056s latency).
All 65535 scanned ports on 172.21.153.20 are closed
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.56 ms 172.21.153.20

Nmap scan report for 172.21.153.135
Host is up (0.00050s latency).
Not shown: 65532 closed ports
PORT    STATE SERVICE VERSION
512/tcp open  exec    netkit-rsh rexecd
513/tcp open  login?
514/tcp open  shell   Netkit rshd
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=512%CT=1%CU=42984%PV=Y%DS=1%DC=D%G=Y%M=080027%T
OS:M=5EB2D1BF%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=108%TI=Z%CI=Z%II=I
OS:%TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O
OS:5=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6
OS:=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O
OS:%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=
OS:0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%
OS:S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(
OS:R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=
OS:N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.50 ms 172.21.153.135

Nmap scan report for 172.21.152.101
Host is up (0.000065s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE VERSION
1716/tcp open  xmsg?
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops

Post-scan script results:
| ssh-hostkey: Possible duplicate hosts
| Key 2048 bb:43:8f:bc:bd:5d:39:22:43:10:ca:9a:59:ab:8f:be (RSA) used by:
|   172.21.152.1
|   172.21.152.79
|   172.21.153.10
| Key 256 10:d2:b0:59:79:cf:fd:58:4b:98:d9:6c:46:ea:3e:16 (ECDSA) used by:
|   172.21.152.1
|   172.21.152.79
|   172.21.153.10
| Key 256 0c:71:d9:f3:21:4c:f2:b2:8a:9b:2b:14:96:ce:2d:1f (ED25519) used by:
|   172.21.152.1
|   172.21.152.79
|_  172.21.153.10
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 512 IP addresses (8 hosts up) scanned in 538.72 seconds
```

However, something went south in printing those services because there were no ports open in device with ip ...10 and ...20.  
I restarted them and ran the command again, a bit differently this time (`-A` but `-sV`):

```console
kali@netsec-kali:~$ sudo nmap -p 1-65535 -sV 172.21.152.101/23
[sudo] password for kali: 
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-06 21:23 CEST
Nmap scan report for 172.21.152.1
Host is up (0.00044s latency).
Not shown: 65529 closed ports
PORT    STATE    SERVICE VERSION
21/tcp  open     ftp     Pure-FTPd
22/tcp  open     ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
80/tcp  open     http    nginx 1.14.2
512/tcp filtered exec
513/tcp filtered login
514/tcp filtered shell
MAC Address: 08:00:27:AB:03:CB (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 172.21.152.44
Host is up (0.00033s latency).
Not shown: 65532 closed ports
PORT    STATE SERVICE    VERSION
25/tcp  open  smtp       Postfix smtpd
143/tcp open  tcpwrapped
993/tcp open  tcpwrapped
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
Service Info: Host:  netsec-peer1.octopus.localdomain

Nmap scan report for 172.21.152.79
Host is up (0.00058s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE         VERSION
79/tcp   open  finger?
443/tcp  open  ssh             OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
4242/tcp open  vrml-multi-use?
9100/tcp open  jetdirect?
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 172.21.152.255
Host is up (0.0029s latency).
All 65535 scanned ports on 172.21.152.255 are closed
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)

Nmap scan report for 172.21.153.10
Host is up (0.00020s latency).
Not shown: 65533 closed ports
PORT      STATE SERVICE VERSION
16765/tcp open  http    lighttpd 1.4.53
22222/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 172.21.153.20
Host is up (0.00016s latency).
All 65535 scanned ports on 172.21.153.20 are closed
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)

Nmap scan report for 172.21.153.135
Host is up (0.00020s latency).
Not shown: 65532 closed ports
PORT    STATE SERVICE VERSION
512/tcp open  exec    netkit-rsh rexecd
513/tcp open  login?
514/tcp open  shell   Netkit rshd
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 172.21.152.101
Host is up (0.0000050s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE VERSION
1716/tcp open  xmsg?

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 512 IP addresses (8 hosts up) scanned in 401.81 seconds
```

Pretty self-explanatory (i just wrote last numbers of it's IPs):
- 101 only has 1716 port open for TCP
- 135 has 3 TCP ports open at 512-514
- 10 and 20 have (still) all 65535 scanned ports closed (weird?) 
- 44 and 79 have both 3 TCP ports open



By printing out `/etc/services` I managed to get the list of the ports with corresponding services.  
I saved it in this dir under the name `ports.txt`.

For the operating systems i used the flag `-O`:

```console
kali@netsec-kali:~$ sudo nmap -p 1-65535 -O 172.21.152.101/23
[sudo] password for kali: 
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-06 21:41 CEST
Nmap scan report for 172.21.152.1
Host is up (0.00075s latency).
Not shown: 65529 closed ports
PORT    STATE    SERVICE
21/tcp  open     ftp
22/tcp  open     ssh
80/tcp  open     http
512/tcp filtered exec
513/tcp filtered login
514/tcp filtered shell
MAC Address: 08:00:27:AB:03:CB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=21%CT=1%CU=31870%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=5EB3134B%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=1%ISR=109%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O5
OS:=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Network Distance: 1 hop

Nmap scan report for 172.21.152.44
Host is up (0.00081s latency).
Not shown: 65534 closed ports
PORT   STATE SERVICE
25/tcp open  smtp
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=25%CT=1%CU=30996%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=5EB3134B%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O5
OS:=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Network Distance: 1 hop

Nmap scan report for 172.21.152.79
Host is up (0.00085s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE
79/tcp   open  finger
443/tcp  open  https
4242/tcp open  vrml-multi-use
9100/tcp open  jetdirect
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=79%CT=1%CU=42905%PV=Y%DS=1%DC=D%G=Y%M=080027%TM
OS:=5EB3134C%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%
OS:TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O5
OS:=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=
OS:FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%
OS:A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0
OS:%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S
OS:=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R
OS:=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N
OS:%T=40%CD=S)

Network Distance: 1 hop

Nmap scan report for 172.21.152.255
Host is up (0.00049s latency).
All 65535 scanned ports on 172.21.152.255 are closed
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop

Nmap scan report for 172.21.153.10
Host is up (0.00050s latency).
Not shown: 65533 closed ports
PORT      STATE SERVICE
16765/tcp open  unknown
22222/tcp open  easyengine
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=16765%CT=1%CU=33525%PV=Y%DS=1%DC=D%G=Y%M=080027
OS:%TM=5EB31365%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=1%ISR=10A%TI=Z%CI=Z%II
OS:=I%TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4
OS:%O5=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%
OS:W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S
OS:=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%R
OS:D=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=
OS:0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U
OS:1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DF
OS:I=N%T=40%CD=S)

Network Distance: 1 hop

Nmap scan report for 172.21.153.20
Host is up (0.00065s latency).
All 65535 scanned ports on 172.21.153.20 are closed
MAC Address: 08:00:27:62:02:EE (Oracle VirtualBox virtual NIC)
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop

Nmap scan report for 172.21.153.135
Host is up (0.00054s latency).
Not shown: 65532 closed ports
PORT    STATE SERVICE
512/tcp open  exec
513/tcp open  login
514/tcp open  shell
MAC Address: 08:00:27:66:17:AB (Oracle VirtualBox virtual NIC)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/6%OT=512%CT=1%CU=39324%PV=Y%DS=1%DC=D%G=Y%M=080027%T
OS:M=5EB31365%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10A%TI=Z%CI=Z%II=I
OS:%TS=A)OPS(O1=M5B4ST11NW4%O2=M5B4ST11NW4%O3=M5B4NNT11NW4%O4=M5B4ST11NW4%O
OS:5=M5B4ST11NW4%O6=M5B4ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6
OS:=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M5B4NNSNW4%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O
OS:%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=
OS:0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%
OS:S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(
OS:R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=
OS:N%T=40%CD=S)

Network Distance: 1 hop

Nmap scan report for 172.21.152.101
Host is up (0.000056s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
1716/tcp open  xmsg
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 512 IP addresses (8 hosts up) scanned in 137.78 seconds
```

But somehow I only managed to get the details for my machine (172.21.152.101):
```
Nmap scan report for 172.21.152.101
Host is up (0.000056s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
1716/tcp open  xmsg
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops
```




```console

```


<center>
<img src=".png">
</center>


```console

```
