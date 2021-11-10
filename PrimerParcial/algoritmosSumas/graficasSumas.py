# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:52:18 2021

@author: Mike
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    datos = pd.read_csv("sumaMax1.csv",sep=";")
    datos2 = pd.read_csv("sumaMax2.csv",sep=";")
    datos4 = pd.read_csv("sumaMax3.csv",sep=";")
    x = datos.N
    y = datos.Tiempo
    y2 = datos2.Tiempo
    y4 = datos4.Tiempo
    plt.plot(x,y,x,y2,x,y4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Version 1 vs Version 2 vs Version 3 ")
    plt.legend(("Version 1", "Version 2", "Version 3"), prop = {"size":10}, loc="upper left")
    plt.grid()
    plt.show()