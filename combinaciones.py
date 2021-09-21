# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:09:47 2021

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

def numCombinaciones(n, r):
    numCom = int(factorial(n) / (factorial(r) * factorial(n - r)))
    return numCom

def combinaciones(r, n):
    s = []
    listaF = []
    for i in range(1, r + 1):
        s.append(i)
    print(s)
    for i in range(1, numCombinaciones(n, r)):
        m = r - 1
        val_max = n
        while(s[m] == val_max):
            m = m - 1
            val_max = val_max - 1
        s[m] = s[m] + 1
        for j in range(m + 1, r):
            s[j] = s[j - 1] + 1
        print(s)

if __name__=="__main__":
    n = 4
    r = 3
    combinaciones(r, n)