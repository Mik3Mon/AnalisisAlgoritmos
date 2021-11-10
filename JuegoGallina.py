# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 03:47:04 2021

@author: Mike
"""
import sistemaExpertoJuego as SE

if __name__=="__main__":
    lobo = True
    maiz = True
    gallina = True
    vivo = True
    estado = True
    posibles = []
    indice = 0
    pierde = True
    print("Juego de la Gallina, el maíz y el lobo")
    while ((maiz|lobo|gallina)):
        SE.estado(maiz, gallina, lobo)
        posibles = SE.movimiento(estado, maiz, gallina, lobo)
        
        vivo = SE.vivo_o_muerto(maiz, gallina, lobo, estado)
        if(vivo):
            selector = int(input("Ingresa lo que deseas hacer "))
            try:
                indice = posibles.index(int(selector))
                maiz, gallina, lobo, estado = SE.sube_al_bote(selector, maiz, lobo, gallina, estado)
            except:
                print("No puede realizar esta acción")
        else:
            pierde = True
            break
    if(pierde):
        print("Lograste pasar a todos al otro lado con exito")
    else:
        print("Perdiste")