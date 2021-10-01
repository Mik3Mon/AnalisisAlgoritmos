# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:43:15 2021

@author: Mike
"""

def metodo_burbuja(lista):
    for i in range(1, len(lista)):
        for j in range(0 , len(lista)-1):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def metodo_seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i,len(lista)):
            if(lista[j] < lista[minimo]):
                minimo = j
        if(minimo != i):
            aux = lista[i]
            lista[i] = lista[minimo]
            lista[minimo] = aux
            
def metodo_insercion(lista):
    for i in range(1,len(lista)):
        valor = lista[i]
        indice = i - 1
        while (i >= 0):
            if(valor < lista[indice]):
                lista[i+1] = lista[i]
                lista[i] = valor
                indice = indice - 1
            else:
                break
                
def metodo_quicksort(lista):
   quicksort_auxiliar(lista,0,len(lista)-1)

def quicksort_auxiliar(lista,primero,ultimo):
   if primero<ultimo:
       puntoDivision = particion(lista,primero,ultimo)
       quicksort_auxiliar(lista,primero,puntoDivision-1)
       quicksort_auxiliar(lista,puntoDivision+1,ultimo)

def particion(lista,primero,ultimo):
   valorPivote = lista[primero]
   marcaIzq = primero+1
   marcaDer = ultimo
   hecho = False
   while not hecho:
       while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1
       while lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1
       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = lista[marcaIzq]
           lista[marcaIzq] = lista[marcaDer]
           lista[marcaDer] = temp
   temp = lista[primero]
   lista[primero] = lista[marcaDer]
   lista[marcaDer] = temp

   return marcaDer

if __name__=="__main__":
    lista = [34,5,23,98,557,34]
    metodo_burbuja(lista)
    metodo_quicksort(lista)
    print(lista)
    print(lista)
    