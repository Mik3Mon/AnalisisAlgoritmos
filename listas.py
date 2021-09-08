# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:35:23 2021

@author: Mike
"""

if __name__=="__main__":
    nombres=["Juan","Rosa","Rebeca"]
    edad=[34,10,23]
    
    print(nombres)
    print(edad)
    
    for i in nombres:
        print(i)
    
    for i in edad:
        print(i*2)
        
    for i in nombres:
        print(len(i))
    
    for i in range(len(nombres)):
        print(nombres[i])
        
    print(max(edad))
    print(max(nombres))
    
    edad.append(10)
    print(max(edad))
    print(edad.count(10))
    
    nombres.extend(edad)
    print(nombres)
    
    edad.sort()
    print(edad)
    
    edad.sort(reverse=True)
    print(edad)
    
    edad.insert(2, 100)
    print(edad)
    
    edad.pop(2)
    print(edad)
    
    edad.remove(10)
    print(edad)