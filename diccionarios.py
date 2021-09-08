# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:34:38 2021

@author: Mike
"""

if __name__=="__main__":
    diccionario={'A0':23,'A1':89,"A2":90}
    print(diccionario)
    diccionario['A2']=100
    print(diccionario)
    
    diccionario2={34:'Rebeca','A0':101}
    
    diccionario2[34]=100
    print(type(diccionario2))
    
    cadena=str(diccionario)
    print(cadena)
    print(type(cadena))
    
    copia1=diccionario.copy()
    
    print(copia1)
    copia1['A1']=2000
    print(diccionario)
    print(copia1)
    
    llaves=[1,2,3,4]
    datos=["A1",'C1',"L1","F45"]
    
    diccionario3=diccionario.fromkeys(llaves,datos[0:2])
    print(diccionario3)
    print(diccionario3[3])
    
    diccionario4={}
    
    for i in range(len(llaves)):
        diccionario4[llaves[i]]=datos[i]
    
    
    print(diccionario4)