# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:44:55 2021

@author: Mike
"""

def predecesor(lista):
    for i in range(1, len(lista)):
        if(len(lista[i]) > len(lista[i-1])):        
            return ([i-1])
    
if __name__=="__main__":
    Lista = ["DANIELA", "MIGUEL", "RUBEN", "HUGO", "DENISSE", "FERNANDO", "PAULINA", "SANTIAGO", "VALENTINA"]
    print(predecesor(Lista))