# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:22:48 2021

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
    for j in range(1,len(lista)):
        i = j - 1
        x = lista[j]
        while (x < lista[i] and i >= 0):
            lista[i+1] = lista[i]
            i = i - 1
        lista[i+1] = x
                
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
    Lista = [-4, -77, -136, 52, -2, -49, 92, -118, -76, 146, 97, 120, -145, -127, 69, 17, 115, -31, -43, -3, -26, -127, -126, -140, -80, -95, -41, -39, 37, 23, -61, 68, -115, -133]
    print("Metodo Burbuja")
    metodo_burbuja(Lista)
    print(Lista)
    print("Metodo Selección")
    metodo_seleccion(Lista)
    print(Lista)
    print("Metodo Inserción")
    metodo_insercion(Lista)
    print(Lista)
    print("Metodo QuickSort")
    metodo_quicksort(Lista)
    print(Lista)