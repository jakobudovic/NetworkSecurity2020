#!/usr/bin/env python3

import socket

host = "localhost"
port = 42424
backlog = 5
size = 1024
     
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(backlog)

conn, clientaddress = s.accept()
data = b""

newdata = conn.recv(size)

# print(data)

while newdata:
	data += newdata
	newdata = conn.recv(size)
if data:
	datastring = data.decode("utf-8")
	print(datastring)

# print(clientaddress)
conn.close()
s.close()
