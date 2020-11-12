#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Diccionar.io")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        listaPalabras=[]
        listaDefiniciones=[]

        lectura(listaPalabras,listaDefiniciones)        #carga en las listas las palabras y las definiciones
        letras=azar(listaPalabras)
        palabra=eligeLaPalabra(listaPalabras,letras)    #elige de la lista de palabras las que contiene dos letra elegidas al azar
        definicion=dameDefinicion(palabra,listaPalabras,listaDefiniciones)  #busca la definicion de la palabra elegida
        lugar=damePosicion(palabra,listaPalabras) #lo puse para ver la posicion de la palabra
        print(listaPalabras) #esto me muestra que se cargan las palabras en listaPalabras
        #print(listaDefiniciones) #esto me muestra que se cargan las definiciones en listaDefiniciones
        print(letras) #lo dejo para ver que letras al azar devuelve al comienzo
        print(palabra) #lo dejo para ver que palabra eligio de la listaPalabras
        print(lugar)
        #print(definicion) #solo muestra la primera definicion, tengo que corregirlo
        cont=5 #este contador son las "vidas"/oportunidades que le quedan al usuario
        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        if candidata=="1":# si escribe 1 significa que no sabe de que palabra se trata
                            cont=cont-1 #en caso de saltear la palabra se descuenta 1 al contador
                            indice=damePosicion(palabra,listaPalabras) #variable de posicion
                            listaPalabras.pop(indice) #aca elimina la palabra que saltea de la lista
                            listaDefiniciones.pop(indice) #elimina la definicion
                            letras=azar(listaPalabras)
                            palabra = eligeLaPalabra(listaPalabras, letras)
                            print(listaPalabras) #solo para ver q devuelve
                            print(letras) #solo para ver q devuelve
                            print(palabra) #solo para ver q devuelve
                            print(indice) #solo para ver q devuelve

                        else:
                            if esCorrecta(candidata,palabra):
                                indice=damePosicion(palabra,listaPalabras) #variable de posicion
                                listaPalabras.pop(indice) #elimina la palabra que acierta de la lista
                                listaDefiniciones.pop(indice) #elimina la definicion
                                puntos += puntuar(candidata, palabra)
                                letras=azar(listaPalabras)
                                print(listaPalabras) #solo para ver que devuelve
                                print(letras) #este print lo puse para ver que me devuelven las letras al azar
                                palabra = eligeLaPalabra(listaPalabras, letras)
                                print(palabra) #lo pongo para ver que palabra es la que sale
                                indice=damePosicion(palabra,listaPalabras) #lo puse para ver la posicion de la palabra
                                print(indice)
                            else:
                                puntos += puntuar(candidata,palabra) #si no acierta la palabra esto hace que le reste puntos
                                cont=cont-1 #si falla una palabra tambien se le descontara una vida
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            if cont==0: #ESTO LO PUSE PARA QUE SE TERMINE EL JUEGO CUANDO SE LE ACABAN LAS VIDAS AL USUARIO
                    segundos=0

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo
            vidasrestantes(screen,cont) #llama a la funcion y muestra en pantalla las "vidas" que le quedan al usuario
            longitud=len(palabra)  #busca la longitud de la nueva palabra
            definicion=dameDefinicion(palabra,listaPalabras,listaDefiniciones) #busca la definicion por si la letra cambio


            dibujar(screen, candidata, longitud, definicion, letras, puntos, segundos)
            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
