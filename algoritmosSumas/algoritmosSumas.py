# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:45:13 2021

@author: Mike
"""

def sumaMaxima(lista):
    tabla=[0]*len(lista)
    for i in range(len(lista)):
        tabla[i] = [0]*len(lista)
    for i in range(len(lista)):
        for j in range(0,i):
            tabla[i][j] = tabla[i-1][j]+lista[i]
        tabla[i][i] = lista[i]
    maximo = tabla[0][0]
    indiceUno = 0
    indiceDos = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if(tabla[i][j] > maximo):
                maximo = tabla[i][j]
                indiceUno = i
                indiceDos = j
    return (maximo,indiceUno,indiceDos)

def sumaMaxima2(lista):
    maximo = 0
    indiceUno = 0
    indiceDos = 0
    tabla=[0]*len(lista)
    for i in range(len(lista)):
        tabla[i] = [0]*len(lista)
    for i in range(len(lista)):
        for  j in range(0,i):
            tabla[i][j] = tabla[i-1][j]+lista[i]
            if(tabla[i][j] > maximo):
                maximo = tabla[i][j]
                indiceUno = i
                indiceDos = j
        tabla[i][i] = lista[i]
        if(tabla[i][i] > maximo):
            maximo = tabla[i][i]
    return (maximo,indiceUno,indiceDos)

def sumaMaxima3(lista):
    maximo = 0
    suma = 0
    for i in range(len(lista)):
        if(suma+lista[i] > 0):
            suma = suma+lista[i]
        else:
            suma = 0
        if(suma > maximo):
            maximo = suma
    return (maximo)

if __name__=="__main__":
    Lista = [107, 38, 104, -59, -77, 81, -78, -94, 115, -145, -135, -81, 137, 
             -62, 125, 58, 33, -7, -107, -139, 70, -105, 117, -23, 94, -47, -66, 
             -101, 20, 61, 43, 83, 128, 8, 71, 97, -114, -65, -134, 17, 65, 28, 
             82, -40, -22, 126, -60, 81, 49, -98, -116, 36, -138, 127, -66, 122, 
             137, 95, 98, 44, -6, 111, -143, 122, 43, 86, -122, 36, 138, -78, 6, 
             68, -116, -30, -129, 115, -47, 142, 34, 80, -146, -25, -80, -138, 134, 
             14, 137, -74, 73, -144, -101, -137, -130, -143, -33, 79, 38, 85, 96, -63]
    print("Version 1")
    print(sumaMaxima(Lista))
    print("Version 2")
    print(sumaMaxima2(Lista))
    print("Version 3")
    print(sumaMaxima3(Lista))
    