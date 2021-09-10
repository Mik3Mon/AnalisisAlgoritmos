# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:50:58 2021

@author: Mike
"""

def sumaMayor(L):
    if len(L) == 0:
        print("Ingresa una lista con datos validos")
    else:
        tmp = 0
        suma2 = 0
        while(tmp <= len(L)):
            suma = 0
            copia = []
            for i in range(tmp, len(L)):
                suma += L[i]
                copia.append(L[i])
                if(suma > suma2):
                    copia2 = copia.copy()
                    suma2 = suma
            tmp = tmp+1
        print("La secuencia de numero que da la suma mayor es: " + str(copia2))
        print('La mayor suma posible es ' + str(suma2))

if __name__=="__main__":
    Lista = [27,6,-50,21,-3,14,16,-8,42,33,-21,9]
    sumaMayor(Lista)
    
    