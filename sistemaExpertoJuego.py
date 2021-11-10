# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 03:17:31 2021

@author: Mike
"""

lobo = True
maiz = True
gallina = True
vivo = True
estado = True
posibles = []
indice = 0
pierde = True

def cambia_estado(entidad):
    if(entidad):
        return False
    else:
        return True
    
def ubicacion(entidad):
    if(entidad):
        return "Derecha"
    else:
        return "Izquierda"

def sube_al_bote(selector, maiz, lobo, gallina, estado):
    if(selector == 1):
        maiz = cambia_estado(maiz)
        estado = cambia_estado(estado)
    elif(selector == 2):
        gallina = cambia_estado(gallina)
        estado = cambia_estado(estado)
    elif(selector == 3):
        lobo = cambia_estado(lobo)
        estado = cambia_estado(estado)
    elif(selector == 0):
        estado = cambia_estado(estado)
    return maiz, gallina, lobo, estado

def estado(maiz, gallina, lobo):
    print("El maiz esta en la " + ubicacion(maiz))
    print("La gallina esta en la " + ubicacion(gallina))
    print("El lobo esta en la " + ubicacion(lobo))
    print("\n")
    
def vivo_o_muerto(maiz, gallina, lobo, estado):
    vivo = True
    if((maiz == gallina) & (estado != (maiz & gallina))):
        vivo = False
        print("La gallina se comio el maiz")
    elif((lobo == gallina) & (estado != (lobo & gallina))):
        vivo = False
        print("El lobo se comio a la gallina")
    return vivo

def movimiento(estado, maiz, gallina, lobo):
    a = []
    a.append(0)
    print("Puede cambiar de lado (escribe 0)")
    if(estado == maiz):
        print("Puede cambiar de lado a el maiz (escribe 1)")
        a.append(1)
    if(estado == gallina):
        print("Puede cambiar de lado a la gallina (escribe 2)")
        a.append(2)
    if(estado == lobo):
        print("Puede cambiar de lado a el lobo (escribe 3)")
        a.append(3)
    print("\n\n")
    return a

def reglas():
    print("")
    
if __name__=="__main__":
    print("Juego de la Gallina, el maíz y el lobo")
    while ((maiz|gallina|lobo)):
        estado(maiz, gallina, lobo)
        posibles = movimiento(estado, maiz, gallina, lobo)
        
        vivo = vivo_o_muerto(maiz, gallina, lobo, estado)
        if(vivo):
            selector = int(input("Ingresa lo que deseas hacer "))
            try:
                indice = posibles.index(int(selector))
                maiz, gallina, lobo, estado = sube_al_bote(selector, maiz, lobo, gallina, estado)
            except:
                print("No puede realizar esta acción")
        else:
            pierde = True
            break
    if(pierde != True):
        print("Lograste pasar a todos al otro lado con exito")
    else:
        print("Perdiste")"""
    

        
        
        
        
        
        
        
        
        