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
    Lista = [107, 38, 104, -59, -77, 81, -78, -94, 115, -145, -135, -81, 137, 
             -62, 125, 58, 33, -7, -107, -139, 70, -105, 117, -23, 94, -47, -66, 
             -101, 20, 61, 43, 83, 128, 8, 71, 97, -114, -65, -134, 17, 65, 28, 
             82, -40, -22, 126, -60, 81, 49, -98, -116, 36, -138, 127, -66, 122, 
             137, 95, 98, 44, -6, 111, -143, 122, 43, 86, -122, 36, 138, -78, 6, 
             68, -116, -30, -129, 115, -47, 142, 34, 80, -146, -25, -80, -138, 134, 
             14, 137, -74, 73, -144, -101, -137, -130, -143, -33, 79, 38, 85, 96, -63]
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