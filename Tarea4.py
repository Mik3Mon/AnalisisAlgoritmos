# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:58:35 2021

@author: Mike
"""


def burbuja(a):
    for i in range(1,len(a)):
        for j in range(0,len(a)-i):
            if(a[j+1] < a[j]):
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux
    print (a)

def seleccion(a):
    for i in range(len(a)):
        minimo = i
        for j in range(i,len(a)):
            if(a[j] < a[minimo]):
                minimo = j
        if(minimo != i):
            aux = a[i]
            a[i] = a[minimo]
            a[minimo] = aux
    print (a)
    
def insercion(a):
    for i in range(1,len(a)):
        valor = a[i]
        indice = i - 1
        while (i >= 0):
            if(valor < a[indice]):
                a[i+1] = a[i]
                a[i] = valor
                indice = indice - 1
            else:
                break
    print (a)
    
if __name__=="__main__":
    
    A=[6,7]
    print("Lista Desordenada")
    print(A)
    print("Lista Ordenada por Burbuja")
    burbuja(A)
    print("Lista Ordenada por Selección")
    seleccion(A)
    print("Lista Ordenada por Inserción")
    insercion(A)