# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:08:39 2021

@author: Mike
"""

from itertools import permutations

if __name__=="__main__":
    lista = [1,2,3,4]
    lista2 = list(permutations(["1","2","3"]))
    listaF = list(set(lista2))
    print(lista2)

    