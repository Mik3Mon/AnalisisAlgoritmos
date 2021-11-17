# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 03:17:31 2021

@author: Mike
"""

persona = True
lobo = True
maiz = True
gallina = True
vivo = True
estado = True
posibles = []
indice = 0
pierde = True

def posicion(persona, maiz, gallina, lobo):
    print("---------------------------------------------")
    print(">>> Ubicacion del jugador, maiz, gallina y lobo <<<\n")
    print("El jugador esta a la " + ubicacion(persona) + " del rio")
    print("El maiz esta a la " + ubicacion(maiz) + " del rio")
    print("La gallina esta a la " + ubicacion(gallina) + " del rio")
    print("El lobo esta a la " + ubicacion(lobo) + " del rio")
    
def sube_al_bote(selector, persona, maiz, gallina, lobo, estado):
    if(selector == 1):
        maiz = cambia_estado(maiz)
        persona = cambia_estado(persona)
        estado = cambia_estado(estado)
    elif(selector == 2):
        gallina = cambia_estado(gallina)
        persona = cambia_estado(persona)
        estado = cambia_estado(estado)
    elif(selector == 3):
        lobo = cambia_estado(lobo)
        persona = cambia_estado(persona)
        estado = cambia_estado(estado)
    elif(selector == 0):
        persona = cambia_estado(persona)
        estado = cambia_estado(estado)
    return persona, maiz, gallina, lobo, estado

def cambia_estado(entidad):
    if(entidad == True):
        return False
    else:
        return True
    
def ubicacion(entidad):
    if(entidad == True):
        return "Izquierda"
    else:
        return "Derecha"  

def vivo_o_muerto(persona, maiz, gallina, lobo, estado):
    vivo = True
    if((maiz == gallina) and (estado != (maiz and gallina))):
        vivo = False
        print("-----------")
        print("Perdiste!!!")
        print("La gallina se comio el maiz")
    elif((lobo == gallina) and (estado != (lobo and gallina))):
        vivo = False
        print("-----------")
        print("Perdiste!!!")
        print("El lobo se comio a la gallina")
    return vivo

def movimiento(persona, maiz, gallina, lobo, estado):
    a = []
    a.append(0)
    print("---------------------------------------------")
    print(">>> Lista de movimientos <<<\n")
    print("Puede cambiar de lado solo al jugador (escribe 0)")
    if(estado == maiz):
        print("Puede cambiar de lado al jugador y el maiz (escribe 1)")
        a.append(1)
    if(estado == gallina):
        print("Puede cambiar de lado al jugador y la gallina (escribe 2)")
        a.append(2)
    if(estado == lobo):
        print("Puede cambiar de lado al jugador y el lobo (escribe 3)")
        a.append(3)
    print("\n")
    return a
    
if __name__=="__main__":
    print("Juego de la Gallina, el maíz y el lobo\n")
    ##reglas()
    while(persona|maiz|gallina|lobo):
        posicion(persona, maiz, gallina, lobo)
        posibles = movimiento(persona, maiz, gallina, lobo, estado)
        vivo = vivo_o_muerto(persona, maiz, gallina, lobo, estado)
        if(vivo == True):
            selector = int(input("Ingresa lo que deseas hacer "))
            try:
                indice = posibles.index(int(selector))
                persona,maiz,gallina,lobo,estado = sube_al_bote(selector, persona, maiz, gallina, lobo, estado)
            except:
                print("No puede realizar esta acción")
        else:
            pierde = False
            break
    if(pierde == True):
        print("----------")
        print("Ganaste!!!")
        print("Lograste pasar a todos al otro lado con exito")
    

        
        
        
        
        
        
        
        
        