# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:48:11 2021

@author: Mike
"""
import metodosOrdenamiento
import random as rn
import copy
from time import time

def crear_lista(longitud):
    lista = []
    for i in range(0,longitud):
        lista.append(rn.randint(0, 200))
    return lista

if __name__=="__main__":
    archivo = open("m3.csv", "w")
    archivo.write("N;Tiempo\n")
    lista = crear_lista(1500)
    x = 100
    for i in range(100,1510,100):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo = time()
        metodosOrdenamiento.metodo_insercion(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 100
    archivo.close()
        