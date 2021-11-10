# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:46:41 2021

@author: Mike
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    datos = pd.read_csv("m1.csv",sep=";")
    datos2 = pd.read_csv("m2.csv",sep=";")
    datos3 = pd.read_csv("m3.csv",sep=";")
    datos4 = pd.read_csv("m4.csv",sep=";")
    x = datos.N
    y = datos.Tiempo
    y2 = datos2.Tiempo
    y3 = datos3.Tiempo
    y4 = datos4.Tiempo
    plt.plot(x,y,x,y2,x,y3,x,y4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja vs Selección vs Inserción vs QuickSort")
    plt.legend(("Burbuja", "Selección", "Inserción", "QuickSort"), prop = {"size":10}, loc="upper left")
    plt.grid()
    plt.show()