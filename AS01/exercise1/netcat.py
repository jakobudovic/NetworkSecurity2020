#!/usr/bin/env python3

import socket

host = "localhost"
port = 42424

s = socket.create_connection((host, port))

stringbuf = ""
for i in range(0, 5):
    stringbuf = stringbuf + "spam " + str(i) + "\n"
    buf = stringbuf.encode("utf-8")

buf = stringbuf.encode("utf-8")

s.sendall(buf)

s.close()


