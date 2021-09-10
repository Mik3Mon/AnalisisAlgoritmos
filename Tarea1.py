# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 03:51:21 2021

@author: Mike
"""

def num_grande(a,b,c):
    grande = a
    if(b > grande):
        grande = b;
    if(c > grande):
        grande = c
    return grande

def num_grande2(a):
    grande = a[0]
    for i in a:
        if(i > grande):
            grande = i
    return grande

def nums_grandes(a):
    if(a[0] > a[1]):
        grande = a[0]
        grande2 = a[1]
    else:
        grande = a[1]
        grande2 = a[0]
    for i in range(2,len(a)):
        if(grande < a[i]):
            grande2 = grande
            grande = a[i]
        else:
            if(grande2 < a[i]):
                grande2 = a[i]
    return grande, grande2

def cad_grande(a):
    
    return

    
if __name__=="__main__":
    Lista = [900,8000,700,0,45,46,100]
    Lista2 = ["Miguel","Juan","Angel","Jose"]
    print("Ejercicio 1")
    print(num_grande(10, 8, 15))
    
    print("Ejercicio 2")
    print(num_grande2(Lista))
    
    print("Ejercicio 3")
    print(nums_grandes(Lista))
    
    
                