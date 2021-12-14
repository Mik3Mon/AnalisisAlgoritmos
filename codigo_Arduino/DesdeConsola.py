# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 22:11:56 2021

@author: Mike
"""

import serial
import time

arduino = serial.Serial("COM2", 9600)
time.sleep(2)

print("Presione 1 para mandar y 2 para apagar: ")

while 1:
    datousuario = input()
    if datousuario == "1":
        arduino.write(b'34.23;34.23;45.22')
        print("Mandar")
    elif datousuario == "2":
        arduino.close()
        print("Apagar")
        break
                      