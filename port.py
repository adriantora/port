#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pyqrcode
import png
import sys
import os

if sys.argv[1] == "-f":
    try:
        f=open(sys.argv[2]).read()
        url = pyqrcode.create(f)
        url.png("url.png",scale=8)
	print(url.terminal(quiet_zone=1))
    except Exception as e:
        print("archivo no encontrado.")
else:
    try:
        url = pyqrcode.create(sys.argv[1])
        url.png("url.png",scale=8)
	print(url.terminal(quiet_zone=1))
    except:
        print("No se a especificado la url.")
