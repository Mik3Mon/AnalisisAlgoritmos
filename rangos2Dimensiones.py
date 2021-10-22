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
    lista = [[21, 1], [7, 26], [6, 24], [25, 5], [14, 25], [9, 15], [23, 2], [3, 11], [1, 10], [7, 12]]
    central = int(len(lista)/2)
    fin = int(len(lista))
    print(central)
    print(lista)
    metodosOrdenamiento.metodo_quicksort(lista)
    print(lista)
    print('El rango del conjunto de punto B es: ' + str(encontrar_rango(central,fin)))