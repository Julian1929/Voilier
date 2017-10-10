#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import socket
IP_Serv = "192.168.10.254"
port = 12800

Sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Sock.bind ((IP_Serv, port))

while True:

    data,addr = Sock.recvfrom (5)

    print data
