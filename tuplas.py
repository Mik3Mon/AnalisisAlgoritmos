# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:16:30 2021

@author: Mike
"""

if __name__=="__main__":
    tupla0=(34,3,56)
    tupla1=(54,45,"Mexico")
    print(tupla0)
    print(tupla0[2])
    print(tupla1[:2])
    
    print(max(tupla0))
    
    lista=list(tupla1)
    print(tupla1)
    print(lista)
    
    lista2=[45,23,"de",67,45]
    
    tupla2=tuple(lista2)
    print(tupla2)
    
    print('de' in tupla2)
    
    print(tupla2.count(45))
    
    datos=("Miguel",4,10,1978)
    nombre,dia,mes,an = datos
    print(nombre + " " + str(dia) + " " + str(mes) + " " + str(an))