# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:41:59 2021

@author: Mike
"""

def factorial(valor):
    bandera = 1
    primera = 1
    segunda = 2
    while (bandera < valor):
        primera = primera * segunda
        segunda = segunda + 1
        bandera = bandera + 1
    return (primera)

def swap(a, indiceUno, indiceDos):
    tmp = a[indiceUno]
    a[indiceUno] = a[indiceDos]
    a[indiceDos] = tmp
    return lista
    
def permutaciones(n):
    s = []
    listaF = []
    for i in n:
        s.append(i)
    print(s)
    listaF.append(list(s))
    for i in range(1, factorial(len(n))):
        m = len(n) - 2
        while(s[m] >= s[m + 1]):
            m = m -1
        k = len(n) - 1
        while(s[m] >= s[k]):
            k = k - 1
        swap(s, m, k)
        p = m + 1
        q = len(n) - 1
        while(p < q):
            swap(s, p, q)
            p = p + 1
            q = q - 1
        if(s not in listaF):
            listaF.append(list(s))
    return listaF
            
if __name__=="__main__":
    lista = [1,1,2,2,2]
    l = permutaciones(lista)
    print(l)
    print(len(l))