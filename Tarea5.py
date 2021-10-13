# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:51:45 2021

@author: Mike
"""

def sumaDigitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

def sumaDigitos2(numero):

if __name__=="__main__":
    print(sumaDigitos(123456789))