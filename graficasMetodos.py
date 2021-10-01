# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:12:27 2021

@author: Mike
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    datos = pd.read_csv("m1.csv",sep=";")
    datos2 = pd.read_csv("m2.csv",sep=";")
    datos4 = pd.read_csv("m4.csv",sep=";")
    x = datos.N
    y = datos.Tiempo
    y2 = datos2.Tiempo
    y4 = datos4.Tiempo
    plt.plot(x,y,x,y2,x,y4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja vs Selección vs Inserción vs ")
    plt.grid()
    plt.show()