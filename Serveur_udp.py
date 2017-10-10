# -*-coding:Latin-1 -*
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import codecs
import socket

#IP_Serv = "192.168.0.230" #IP Raspi
IP_Serv = "127.0.0.1"
port = 12800

ID = 65
TAILLE = 5
VVENT = 50
DVENT = 128
GITE = 12

sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind ((IP_Serv, port))

while True:

    data,addr = sock.recvfrom (13) #ligne de décodage des trames.
    print "ID du systeme", ord (data[0])
    print "Taille de la trame", ord (data[1])
    print "Position de la GV", ord (data[2])
    print "Position du safran", ord (data[3])

    trame_reponse = bytearray([ID, TAILLE, VVENT, DVENT, GITE]) #bytearray creer un tableau.
            
    sock.sendto(trame_reponse, addr)


    print ""
    print ""
    print "0000000000000000000000000000000000 NE FONCTIONNE PAS !!!!!! 00000000000000000000000000000000000"




    lat1 = 1651782
    #lon1 = 21.0122287
    #lat2 = 52.406374
    #lon2 = 16.9251681

    b3=(lat1>>24)
    b2=(lat1>>16)&0xFF
    b1=(lat1>>8)&0xFF
    b0=(lat1>>0)&0xFF

    print ""
    print ""
    print "latittude", lat1
    print " Vakeur Hexa de b2 : ", hex(b2)
    print " Vakeur Hexa de b1 : ", hex(b1)
    print " Vakeur Hexa de bo : ", hex(b0)

    reponse = bytearray([ID]) #bytearray creer un tableau.

    print "ID du systeme", ord (data[0])
