import socket
IPdest = "192.168.0.230"
Portdest = 12800

sock= socket.socket (socket.AF_INET,socket.SOCK_DGRAM)

sock.sendto("Salut",(IPdest,Portdest))
