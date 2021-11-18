# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 00:22:54 2021

@author: crist
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import pprint
import math

def metodo_quicksort(lista):
   quicksort_auxiliar(lista,0,len(lista)-1)

def quicksort_auxiliar(lista,primero,ultimo):
   if primero<ultimo:
       puntoDivision = particion(lista,primero,ultimo)
       quicksort_auxiliar(lista,primero,puntoDivision-1)
       quicksort_auxiliar(lista,puntoDivision+1,ultimo)

def particion(lista,primero,ultimo):
   valorPivote = lista[primero]
   marcaIzq = primero+1
   marcaDer = ultimo
   hecho = False
   while not hecho:
       while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1
       while lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1
       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = lista[marcaIzq]
           lista[marcaIzq] = lista[marcaDer]
           lista[marcaDer] = temp
   temp = lista[primero]
   lista[primero] = lista[marcaDer]
   lista[marcaDer] = temp

   return marcaDer

def graficas(puntos):
    for indice in range(len(puntos)):
        x.append(int(puntos[indice][0]))
        y.append(int(puntos[indice][1]))
    line, =ax.plot(x,y,'o',picker=5)
    
    puntosSeleccionado=fig.canvas.mpl_connect('pick_event',onpick)
    plt.show()
def onpick(event):
    thisline=event.artist
    xdata=thisline.get_xdata()
    ydata=thisline.get_ydata()
    ind=event.ind
    listaPunto=[]
    puntoSeleccionado=tuple(zip(xdata[ind],ydata[ind]))
    listaPunto.append(puntoSeleccionado[0][0])
    listaPunto.append(puntoSeleccionado[0][1])
    print(listaPunto)
    segundaVentana(listaPunto)

def segundaVentana(listaPunto):
    figDos=plt.figure()
    a=figDos.add_subplot(111)
    a.set_title('rango del punto seleccionado')
    puntos=encontrar_rangos(listaPunto[0],listaPunto[1])
    a.text(listaPunto[0]+.7, listaPunto[1]+.7, puntos, fontsize=12, color = "r", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='right')
    print(puntos)
    line, =a.plot(x,y,'*',picker=5)
    line, =a.plot((listaPunto[0]),(listaPunto[1]),'*', picker=5)


def encontrar_rangos(punto,punto2):
    rango=0
    for i in range(len(lista)):
        if punto == lista[i][0]:
            if punto2==lista[i][1]:
                j=punto
                for j in range(i):
                    
                    if lista[j][0]<lista[i][0] and lista[j][0]!=lista[i][0]:
                        if lista[j][1]<lista[i][1]:
                            rango+=1
                    else:
                        pass
                
    return 'rango: '+str(rango)
            
if __name__=="__main__":
    lista=[[21, 1], [8, 26], [6, 24], [25, 5], [14, 25], [9, 15], [24, 2], [24, 11], [1, 10], [7, 12]]
    rangoi=0
    metodo_quicksort(lista)
    print(lista)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_title('Escoja puntos')
    puntosSeleccionado={}
    x=[]
    y=[]
    graficas(lista)
    