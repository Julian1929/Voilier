# -*-coding:Latin-1 -*
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import socket

class VoilierClient:


    def __init__(self):
        self.nom = "Mesures"
        self.IP_Serv = "0.0.0.0"
        self.port = 0
        self.safran = 0
        self.grandvoile = 0
        self.gite = 0
        self.latitude = 0
        self.longitude = 0
        self.vitesseduvent = 0
        self.directionduvent = 0
        self.id=0
        

    def initCom(self,ip, port):
        self.IP_Serv = ip
        self.port= port
        print "adresse du serveur :", self.IP_Serv
        print "port du serveur :", self.port
        try:
            self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        except socket.error as msg:
            return msg
        return -1

    def txrx(self):
        trame_envoi = bytearray([self.id,2,self.grandvoile,self.safran]) #bytearray creer un tableau.
        self.sock.sendto(trame_envoi, (self.IP_Serv, self.port))
         
        trame_reponse,addr = self.sock.recvfrom (13) #ligne de décodage des trames.

        b3=ord(trame_reponse[4])
        b2=ord(trame_reponse[5])
        b1=ord(trame_reponse[6])
        b0=ord(trame_reponse[7])

        lat = b3<<24 | b2<<16 | b1<<8 | b0
        if b3 > 127:
            lat=(~lat)&0XFFFFFFFF
            lat=lat+1
            lat=lat*(-1)

        self.latitude=float(lat)/10000000

        b3=ord(trame_reponse[8])
        b2=ord(trame_reponse[9])
        b1=ord(trame_reponse[10])
        b0=ord(trame_reponse[11])

        lon = b3<<24 | b2<<16 | b1<<8 | b0
        if b3 > 127:
            lon=(~lon)&0XFFFFFFFF
            lon=lon+1
            lon=lon*(-1)
            
        self.longitude=float(lon)/10000000

        


        
        self.id+=1

monVoilier = VoilierClient()
monVoilier.initCom("127.0.0.1",12800)
monVoilier.safran=25
monVoilier.grandvoile=65
monVoilier.txrx()
print monVoilier.latitude
print monVoilier.longitude
