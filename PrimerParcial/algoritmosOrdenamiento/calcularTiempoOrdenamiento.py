# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:45:39 2021

@author: Mike
"""

import metodosOrdenamiento
import random as rn
import copy
from time import time

def crear_lista(longitud):
    lista = []
    for i in range(0,longitud):
        lista.append(rn.randint(-500, 500))
    return lista

if __name__=="__main__":
    archivo = open("m1.csv", "w")
    archivo.write("N;Tiempo\n")
    lista = crear_lista(15000)
    x = 100
    for i in range(100,15010,100):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        metodosOrdenamiento.metodo_burbuja(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 100
    archivo.close()
    archivo = open("m2.csv", "w")
    archivo.write("N;Tiempo\n")
    x = 100
    for i in range(100,15010,100):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        metodosOrdenamiento.metodo_seleccion(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 100
    archivo.close()
    archivo = open("m3.csv", "w")
    archivo.write("N;Tiempo\n")
    x = 100
    for i in range(100,15010,100):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        metodosOrdenamiento.metodo_insercion(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 100
    archivo.close()
    archivo = open("m4.csv", "w")
    archivo.write("N;Tiempo\n")
    x = 100
    for i in range(100,15010,100):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        metodosOrdenamiento.metodo_quicksort(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 100
    archivo.close()