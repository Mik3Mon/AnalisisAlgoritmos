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

def sumaDigitos2(Lista):
    if len(Lista) == 0:
        return 0 
    else:
        return int(Lista[0]) + sumaDigitos2(Lista[1:])

if __name__=="__main__":
    Lista = "456"
    print("Iterativo")
    print(sumaDigitos(123456789))
    print("Recursivo")
    print(sumaDigitos2(Lista))
    
    