# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:58:07 2021

@author: Mike
"""

def predecesor(lista):
    for i in range(1, len(lista)):
        if(lista[i] < lista[i-1]):        
            return (print(lista[i-1]))
    
if __name__=="__main__":
    Lista = ["TOMAS", "BRUNO", "ELIE", "DAN", "ZEKE", "DANIELA", "MIGUEL", "RUBEN", "HUGO"]
    predecesor(Lista)