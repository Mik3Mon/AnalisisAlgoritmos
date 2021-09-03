# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:49:59 2021

@author: Mike
"""
def funcionUno(a):
    print(a*2)
    
def funcionDos(a):
    return len(a)
    
if __name__=="__main__":
    cadena="México siempre fiel"
    print(cadena)
    
    #recorrer la cadena
    print(cadena[0:6])
    print(cadena[7:])
    print(cadena[:8])
    print(cadena[-4:])
    print(cadena[:-5])
    
    print(len(cadena))
    
    print(cadena.split())
    print(cadena.split("e"))
    
    print(cadena*3)
    
    nueva_cadena="m" + cadena[1:]
    print(nueva_cadena)
    
    cadena=cadena.replace("M", "m")
    print(cadena)
    
    cadena=cadena.replace("s", "")
    print(cadena)
    
    if("sapo" in cadena):
        print("si esta")
    else:
        print("no esta")
    if(len(cadena)>7):
        print("mayor o igual a 7")
    
    funcionUno(cadena)
    funcionUno(23)