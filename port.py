#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pyqrcode
import png
import sys
import os
from  minserv import *

#revisar sus usos para limpiar
import socket
import fcntl
import struct

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    ip = s.getsockname()[0]

    return ip


def generador(text):
    url = pyqrcode.create(text)
    url.png("/tmp/image.png",scale=8)
    print(url.terminal(quiet_zone=1))

if len(sys.argv) == 1:
    print("Write text: ")
    texto=raw_input()
    generador(texto)
else:

    if len(sys.argv) > 0:
        if sys.argv[1] != "--import" and sys.argv[1] != "-f":
            generador(sys.argv[1])

        if sys.argv[1] == "--import":
            ip=get_lan_ip()if len(sys.argv) > 1:
            port=5000
            print ip+":"+str(port)
            generador(ip+":"+str(port))
            minserver(ip,port)#recibir la informacion de la funcion.
    
        #mostrador de archivos especificado con "-f"
        if sys.argv[1] == "-f":
            try:
                f=open(sys.argv[2]).read()
                generador(f)
            except Exception as e:
                print("File not found.")
