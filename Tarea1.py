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
    grande = a[0]
    grande2 = a[0]
    for i in a:
        if(i > grande):
            grande = i
            for j in a:    
                if(j > grande2 and j < grande):
                    grande2 = j
    return grande, grande2

def cad_grande(a):
    
    return

    
if __name__=="__main__":
    print("Ejercicio 1")
    print(num_grande(10, 8, 15))
    
    print("Ejercicio 2")
    Lista = [10,80,7,0,45,46]
    print(num_grande2(Lista))
    
    print("Ejercicio 3")
    print(nums_grandes(Lista))
    
    
                