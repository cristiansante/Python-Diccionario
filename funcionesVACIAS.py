# -*- coding: UTF-8 -*-
from principal import *
from configuracion import *

import random
import math

def lectura(listaPalabras,listaDefiniciones): #cargar en las listaPalabras las palabras y en listaDefiniciones las definiciones
    archivo=open("diccionario.txt", "r") #abre el archivo diccionario

    a=archivo.readlines() #lee todas las lineas del archivo

    cadena=""
    listanombre=listaPalabras
    listadefinicion=listaDefiniciones

    for i in a: #recorro linea por linea
        for j in i:
            if j!=":" and j!="\n": #si el caracter es distinto a ":" o salto de linea lo agrega a la cadena
                if j=="ó":
                    j="o"
                cadena=cadena+j #lleno la cadena
            else:
                if j==":":
                    listanombre.append(cadena) #cuando encuentre ":" va a mandar la cadena a la lista y despues vaciar la cadena
                    cadena="" #reinicio la cadena para volver a usarla
                else:
                    listadefinicion.append(cadena) #va a seguir recorriendo la linea y lo q esta despues de los ":" y antes del salto de linea lo va a mandar a la lista de definiciones
                    cadena=""
    archivo.close()

def eligeLaPalabra(listaPalabras, cadenaDe2Letras): #elige de la lista de palabras una que contiene estas letras
    cadena="" #aca se guarda la palabra elegida
    cont=0
    for i in listaPalabras:
        for k in cadenaDe2Letras: #recorre las 2 letras
            if (esta(k,i)): #si la letra esta en la palabra el contador suma 1
                cont=cont+1
        if cont==2: #si cuando termina el for el cont es 2 se va a guardar la palabra en la cadena vacia
            cadena=i
        cont=0 #se reinicia el contador para el siguiente ciclo
    return(cadena)

def damePosicion(palabra,listaPalabras): #devuelve la posicion de un elemento en una lista de elementos
    for i in range(len(listaPalabras)): #recorre la lista de palabras
        if listaPalabras[i]==palabra: #si la palabra esta en la lista me devuelve la posicion de esa palabra
            return(i)

def dameDefinicion(palabra,listaPalabras,listaDefiniciones): #devuelve la definicion de la palabra
    for i in range(len(listaPalabras)): #recorre la lista palabras
        if listaPalabras[i]==palabra: #si la palabra coincide en la lista que me devuelva el contenido de la misma posicion pero de la listaDefiniciones
            return(listaDefiniciones[i])

def azar(listaPalabras): #elige 2 letras al azar
    azar=[] #aca van a ir las 2 letras al azar
    cont=0

    palabraalazar=random.choice(listaPalabras) #elige una palabra al azar de la lista (NO necesariamente esto quiere decir que va a salir esta palabra, solo lo hago para garantizar que si o si las 2 letras esten en alguna palabra)
    while cont!=2:
        letraalazar=random.choice(palabraalazar) #aca elige una letra al azar de esa palabra
        if not(esta(letraalazar,azar)): #si la letra no esta en la lista vacia va a entrar con el siguiente append
            azar.append(letraalazar)
            cont=cont+1 #cada vez que agregue una letra el cont sumara 1, cuando llegue a 2 se corta el while
    return(azar)

def puntuar(candidata,palabra): #suma puntos si es correcta, suma distinto para vocales, consonantes faciles, consonantes dificiles y longitud.
    puntos=0
    if esCorrecta(candidata,palabra): #solo si es correcta va a suceder lo siguiente
        for i in palabra: #reccore la palabra y dependiendo que letra es suma distinta cantidad de puntos
            if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
                puntos=puntos+1
            else:
                if i=="j"or i=="k" or i=="q" or i=="w" or i=="x" or i=="y" or i=="z":
                    puntos=puntos+5
                else:
                    puntos=puntos+2
    return(puntos)

def esCorrecta(candidata, palabra): # Devuelve verdadero si acierta falso en caso contrario
    if candidata==palabra: #si son iguales devuelve un True
        return(True)
    else:
        return(False)

def esta(palabra, listaPalabras):
    for i in listaPalabras: #recorre la listaPalabras y si la palabra esta en la lista devuelve True
        if i==palabra:
            return(True)
    return(False)

def vidasrestantes(screen,contador): #esta funcion muestra las vidas del usuario
    #Texto vidas restantes
    fuente= pygame.font.Font( pygame.font.get_default_font(), 22) #esto elige el tipo de lecha y el tamaÃ±o
    textovidas=fuente.render("Vidas restantes:",1,(255,255,255)) #el texto y su color
    screen.blit(textovidas,(270,7)) #la posicion en pantalla de "vidas restantes"
    #numero vidas restanes
    if contador>1: #mantiene el mismo color si es mayor a 1
        numerovidas=fuente.render(str(contador),1,(255,255,255))
        screen.blit(numerovidas,(452,7)) #posicion en pantalla del contador
    else: #esto pone en color rojo el color de las vidas restantes si queda 1
        numerovidas=fuente.render(str(contador),1,(255,0,0))
        screen.blit(numerovidas,(452,7))