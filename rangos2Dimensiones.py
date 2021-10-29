# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 01:04:24 2021

@author: Mike
"""
import metodosOrdenamiento

def encontrar_rango(central,fin):
    rango=0
    rango_total=0
    for i in range(central,len(lista)):
        j=i
        while(j >= 0):
            if lista[i][1:]>lista[j][1:]:
                rango+=1
            j-=1
    return rango


if __name__=="__main__":
    lista = [[1,10],[3,11],[6,24],[7,12],[7,26],[9,15],[14,25],[21,1],[23,2],[25,5]]
    central = len(lista)//2
    fin = len(lista)-1
    print(central)
    print(fin)
    print(lista)
    metodosOrdenamiento.metodo_quicksort(lista)
    print(lista)
    print('El rango del conjunto de punto B es: ' + str(encontrar_rango(central,fin)))