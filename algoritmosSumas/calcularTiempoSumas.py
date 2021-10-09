# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:47:14 2021

@author: Mike
"""

import algoritmosSumas
import random as rn
import copy
from time import time

def crear_lista(longitud):
    lista = []
    for i in range(0,longitud):
        lista.append(rn.randint(-150, 150))
    return lista

if __name__=="__main__":
    archivo = open("sumaMax1.csv", "w")
    archivo.write("N;Tiempo\n")
    lista = crear_lista(100)
    x = 2
    for i in range(100,150,2):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        algoritmosSumas.sumaMaxima(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 2
    archivo.close()
    archivo = open("sumaMax2.csv", "w")
    archivo.write("N;Tiempo\n")
    x = 2
    for i in range(100,150,2):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        algoritmosSumas.sumaMaxima2(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 2
    archivo.close()
    archivo = open("sumaMax3.csv", "w")
    archivo.write("N;Tiempo\n")
    x = 2
    for i in range(100,150,2):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        algoritmosSumas.sumaMaxima3(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 2
    archivo.close()
    print(lista)
    print(algoritmosSumas.sumaMaxima(lista))
    print(algoritmosSumas.sumaMaxima2(lista))
    print(algoritmosSumas.sumaMaxima3(lista))