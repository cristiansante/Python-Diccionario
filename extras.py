import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    elif key == K_1:
       return("1")
    else:
        return("")


def dibujar(screen, candidata, longitud, definicion, letras, puntos, segundos):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGRANDE= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea de abajo
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #para mostrar los segundos, en rojo si quedan menos de 15
    if puntos<100 and puntos>=0: #hago este if para cuando el usuario tenga una puntuacion entre esos numeros sea del color del texto
        ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    else:
        ren1 = defaultFont.render("Puntos: " + str(puntos), 1, LETRAS_AZAR) #si es distinta a cualquiera de las opciones previas va a ser del color LETRAS_AZAR
    if(segundos<15):
        ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    #para mostrar las letras que surgieron al azar
    ren3 = defaultFontGRANDE.render(letras[0]+"  "+letras[1], 1, LETRAS_AZAR) #MODIFIQUE COLOR_TIEMPO_FINAL POR LETRAS_AZAR

    for i in range(longitud): #muestra los _
        screen.blit(defaultFont.render("_", 1, COLOR_LETRAS), (170+TAMANNO_LETRA*2*i,350)) #MODIFIQUE EL 200 POR UN 170 PARA QUE LA PALABRA "INTERVENCIONISMO" ENTRARA SIN SALIRSE DE PANTALLA

    for i in range(len(candidata)): #muestra las letras que escribe el jugador, las ubica sobre los _
        screen.blit(defaultFont.render(candidata[i], 1, COLOR_LETRAS), (170+TAMANNO_LETRA*2*i,350)) #MODIFIQUE EL 200 POR UN 170 PARA QUE LA PALABRA "INTERVENCIONISMO" ENTRARA SIN SALIRSE DE PANTALLA

    #para mostrar la definicion

    x=40
    y=60
    for letra in definicion:
        if (x>ANCHO-250) and letra==" ": #aca si la letra supera el limite y ademas es un espacio va a bajar de renglon, de esta manera no se cortan las palabras de las definiciones
            x=40 #empieza el siguiente renglon en esta posicion
            y=y+TAMANNO_LETRA
        else:
            x=x-1 #si no se cumple lo anterior le resto 1 a X para asi buscar un espacio
        screen.blit(defaultFont.render(letra, 1, COLOR_LETRAS), (x,y))
        x=x+TAMANNO_LETRA

    screen.blit(ren1, (680, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (ANCHO/2-TAMANNO_LETRA, 550)) #muestra las letras que salieron al azar