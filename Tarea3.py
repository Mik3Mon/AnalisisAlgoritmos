# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:42:09 2021

@author: Mike
"""

def maxSuma(lista):
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

def maxSuma2(lista):
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
    datos = [27,6,-50,21,-3,14,16,-8,42,33,-21,9]
    maximo,rango1,rango2=maxSuma(datos)
    print("Primera Forma")
    print(maximo)
    print(datos[rango2:rango1+1])
    print("Sgunda Forma")
    print(maxSuma2(datos))