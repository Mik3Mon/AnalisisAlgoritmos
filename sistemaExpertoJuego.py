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
pierde = True

def posicion(persona, maiz, gallina, lobo):
    print("\n---------------------------------------------\n")
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
        print("\n-----------\n")
        print("Perdiste!!!")
        print("La gallina se comio el maiz")
    elif((lobo == gallina) and (estado != (lobo and gallina))):
        vivo = False
        print("\n-----------\n")
        print("Perdiste!!!")
        print("El lobo se comio a la gallina")
    return vivo

def movimiento(persona, maiz, gallina, lobo, estado):
    a = []
    a.append(0)
    print("\n---------------------------------------------\n")
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
    return a

def reglas():
    print("\n---------------------------------------------\n")
    print(">>> Objetivo <<<\n")
    print("El objetivo principal de este juego es conseguir cruzar a todos los personajes al otro lado del rio.")
    print("Inicialmente comenzamos en el lado izquierdo de un rio virtual siendo el jugador, un maiz, una gallina y un lobo,")
    print("El juego consiste en pasar de un lado a otro mediante un barco, pero en este unicamente caben 2 personajes, el chiste es hacer")
    print("la combinacion correcta de movimientos para que todos los personajes se mantengan con vida, en el momento que uno muera se "
          + "acaba el juego")
    print("\n>>> Observaciones <<<\n")
    print("1.- En el barco unicamente caben 2 personajes, uno es el jugador por default y el otro cualquier personaje")
    print("2.- El jugador es el unico que puede moverse en el barco solo")
    print("3.- En todo momento se mencionara al jugador las posiciones de todos los personajes y los movimientos que puede realizar al "
          + "estar de un lado o del otro lado del rio")
    print("Divierte!!")

def juegoGallina():
    persona = True
    lobo = True
    maiz = True
    gallina = True
    vivo = True
    estado = True
    posibles = []
    pierde = True
    print("Juego de la Gallina, el maíz y el lobo")
    reglas()
    while(persona|maiz|gallina|lobo):
        posicion(persona, maiz, gallina, lobo)
        posibles = movimiento(persona, maiz, gallina, lobo, estado)
        vivo = vivo_o_muerto(persona, maiz, gallina, lobo, estado)
        if(vivo == True):
            selector = int(input("> Ingresa lo que deseas hacer < "))
            try:
                indice = posibles.index(int(selector))
                persona,maiz,gallina,lobo,estado = sube_al_bote(selector, persona, maiz, gallina, lobo, estado)
            except:
                print("No puede realizar esta acción")
        else:
            pierde = False
            break
    if(pierde == True):
        posicion(persona, maiz, gallina, lobo)
        print("\nGanaste!!!")
        print("Lograste pasar a todos al otro lado con exito")

if __name__=="__main__":
    juegoGallina()

        
        
        
        
        
        
        
        
        