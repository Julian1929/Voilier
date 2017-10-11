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

# Définition de la Longitude et Lattitude.

    lat = 1651782
    b3=(lat>>24)&0xFF
    b2=(lat>>16)&0xFF
    b1=(lat>>8)&0xFF
    b0=(lat>>0)&0xFF

    lon = 1651782
    b7=(lon>>24)&0xFF
    b6=(lon>>16)&0xFF
    b5=(lon>>8)&0xFF
    b4=(lon>>0)&0xFF


    data,addr = sock.recvfrom (13) #ligne de décodage des trames.
    print "ID du systeme", ord (data[0])
    print "Taille de la trame", ord (data[1])
    print "Position de la GV", ord (data[2])
    print "Position du safran", ord (data[3])

    trame_reponse = bytearray([ID, TAILLE, VVENT, DVENT, b3,b2,b1,b0,b7,b6,b5,b4,GITE]) #bytearray creer un tableau.
            
    sock.sendto(trame_reponse, addr)


    print ""
    print ""
    print "Longitude et Lattitude"
    print "Lattitude", lat
    print ""
    #print "Valeur en héxa de b3", hex(b3)
    #print "Valeur en héxa de b2", hex(b2)
    #print "Valeur en héxa de b1", hex(b1)
    #print "Valeur en héxa de b0", hex(b0)

    print "Longitude", lon
    #print "Valeur en héxa de b7", hex(b7)
    #print "Valeur en héxa de b6", hex(b6)
    #print "Valeur en héxa de b5", hex(b5)
    #print "Valeur en héxa de b4", hex(b4)



    

    #LAT = 1651782
    #lon1 = 21.0122287
    #lat2 = 52.406374
    #lon2 = 16.9251681

    #b3=(LAT>>24)
    #b2=(LAT>>16)&0xFF
    #b1=(LAT>>8)&0xFF
    #b0=(LAT>>0)&0xFF
#
 #   print "ID du systeme", ord (data[0])
  #  print ""
   # print ""
 #   print "latittude", ord (data[2])
  #  print " Vakeur Hexa de b2 : ", hex(b2)
   # print " Vakeur Hexa de b1 : ", hex(b1)
#    print " Vakeur Hexa de bo : ", hex(b0)

#    trame_reponse = bytearray([ID, LAT]) #bytearray creer un tableau.


    
