#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import socket

#UDP_IP = "192.168.0.230" #IP Raspi
UDP_IP = "127.0.0.1"

UDP_PORT = 12800
DATAGRAM = 2
ID = 51
TAILLE = 5
SAFRAN = 23
GV = 32


MESSAGE = bytearray([ID,TAILLE,GV,SAFRAN]) #bytearray creer un tableau.

print ""
print "-----------------------------------------------"
print "             DEMANDE AU SERVEUR                "
print "-----------------------------------------------"
print ""

print "message:", MESSAGE
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "longeur du datagram : ", DATAGRAM
print "ID du systeme : ", ID
print "Taille de la trame : ", TAILLE
print "Position du safran : ", SAFRAN, "Position de la grand voile : ",GV

 
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

print ""
print "-----------------------------------------------"
print "             REPONSE DU SERVEUR:               "
print "-----------------------------------------------"
print ""
trame_reponse,addr = sock.recvfrom (13) #ligne de décodage des trames.

b3=ord(trame_reponse[4])
b2=ord(trame_reponse[5])
b1=ord(trame_reponse[6])
b0=ord(trame_reponse[7])

lat = b3<<24 | b2<<16 | b1<<8 | b0
if b3 > 127:
    print "latitude negative"
    lat=(~lat)&0XFFFFFFFF
    lat=lat+1
    lat=lat*(-1)
lat_f=float(lat)/10000000

b3=ord(trame_reponse[8])
b2=ord(trame_reponse[9])
b1=ord(trame_reponse[10])
b0=ord(trame_reponse[11])

lon = b3<<24 | b2<<16 | b1<<8 | b0
if b3 > 127:
    print "longitude negative"
    lon=(~lon)&0XFFFFFFFF
    lon=lon+1
    lon=lon*(-1)
lon_f=float(lon)/10000000



print "trame du voilier :",trame_reponse.encode("hex")
print "ID du systeme", ord (trame_reponse[0])
print "Taille de la trame", ord (trame_reponse[1])
print "VVENT", ord (trame_reponse[2])
print "Direction du vent", ord (trame_reponse[3])
print " ";
print  "lattitude:", lat_f;
print " ";
print "longitude:", lon_f; #le chiffre correspond à la place dans la trame
print " ";
print "gite du bateau", ord (trame_reponse[8])


print "-----------------------------------------------"
print "                 FIN DE TRAME                  "
print "-----------------------------------------------"
    
