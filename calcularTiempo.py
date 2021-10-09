# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:48:11 2021

@author: Mike
"""
import metodosOrdenamiento
import sumaMaxima
import Tarea3
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
        sumaMaxima.sumaMaxima(lista_nueva)
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
        Tarea3.maxSuma(lista_nueva)
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
        Tarea3.maxSuma2(lista_nueva)
        transcurrido = time() - inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,".5f")+"\n")
        x = x + 2
    archivo.close()
    print(lista)
    print(sumaMaxima.sumaMaxima(lista))
    print(Tarea3.maxSuma(lista))
    print(Tarea3.maxSuma2(lista))