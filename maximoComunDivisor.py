# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 19:20:14 2021

@author: Mike
"""

def mcd(a,b):
    if b == 0:
        return a
    else:
        c = a % b
        return mcd(b, c)

if __name__=="__main__":
    print(mcd(124, 6))
    
    print(mcd(8, 12))
    
    print(mcd(3473, 78700))