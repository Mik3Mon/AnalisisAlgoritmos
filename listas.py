# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:35:23 2021

@author: Mike
"""

if __name__=="__main__":
    nombres=["Juan","Pedro","Rebeca"]
    edad=[34,10,'23']
    
    print(nombres)
    print(edad)
    
    for i in nombres:
        print(i)
    
    for i in edad:
        print(i*2)
        
    for i in nombres:
        print(len(i))