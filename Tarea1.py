# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 03:51:21 2021

@author: Mike
"""

def MAX(a,b,c):
    grande = a
    if(b > grande):
        grande = b;
    if(c > grande):
        grande = c
    return grande

def MAX2(a):
    grande = a[0]
    for i in a:
        if(i > grande):
            grande = i
    return grande

    
if __name__=="__main__":
    print("Ejercicio 1")
    print(MAX(10, 8, 15))
    
    print("Ejercicio 2")
    Lista = [10,15,7,0,45,46]
    print(MAX2(Lista))
    
    
                