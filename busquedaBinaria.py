# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 20:22:48 2021

@author: Mike
"""

def busquedaBinaria(Lista, clave, inferior = 0, superior = 0):
    if(superior == 0):
        superior = len(Lista)-1
    central = (inferior + superior) // 2
    if(Lista[central] == clave):
        return central
    else:
        if(Lista[central] < clave):
            return busquedaBinaria(Lista, clave, inferior = central+1, superior = superior)
        if(Lista[central] > clave):
            return busquedaBinaria(Lista, clave, inferior = 0, superior = central)
    
    
if __name__=="__main__":
    Lista = [3,8,15,25,95,100,153,1456] 
    print(busquedaBinaria(Lista, 15))
    