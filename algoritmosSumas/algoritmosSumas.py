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