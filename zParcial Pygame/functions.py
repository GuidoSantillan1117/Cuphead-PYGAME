import pygame
from personaje_principal import Personaje
from personaje_principal_nave import PersonajeNave
from boss import BossFinal
from colisiones import *
from hitbox import *
from ranking import *

def mostrar_flecha_win(pantalla,posicion_x,posicion_y):
    imagen = pygame.image.load("zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/image (1).png")
    imagen_reescalada = pygame.transform.scale(imagen,(100,50))
    pantalla.blit(imagen_reescalada,(posicion_x,posicion_y))

def dibujar_string_pantalla(pantalla,font,numero,posicion,color):
    dibujo_string = font.render(str(numero),True,color)
    rect_dibujo = dibujo_string.get_rect()
    rect_dibujo.center = (posicion) 
    pantalla.blit(dibujo_string,rect_dibujo)

def dibujar_score_menu_principal(pantalla,font,score:int,score_completo_nivel,score_extra,width):
    string_score = f"Score: {str(score)} (Puntos por completar nivel: {str(score_completo_nivel)} + Puntos extras por tiempo: {str(score_extra)}) "
    dibujo_score = font.render(string_score,True,"Black")
    rect_score = dibujo_score.get_rect()
    rect_score.center = (width //2, 40)
    pantalla.blit(dibujo_score,rect_score)

def dibujar_mensaje_alerta(pantalla,font,posicion):
    string_mensaje_alerta = "ALERTA: Seleccionar el NIVEL 1 reiniciara el SCORE!"
    dibujo_string_alerta = font.render(string_mensaje_alerta,True,"Red")
    rect_alerta = dibujo_string_alerta.get_rect()
    rect_alerta.center = (posicion)
    pantalla.blit(dibujo_string_alerta,rect_alerta)

def dibujar_nombre(pantalla,nombre_ingresado,font,posicion):
    texto_superficie = font.render(nombre_ingresado, True, "Black")

    pantalla.blit(texto_superficie,posicion)

def dibujar_valores_pantalla(screen, font, lista_datos):
    posicion_y = 240  
    for fila in lista_datos:
        texto = f"ID: {fila[0]}, Nombre: {fila[1]}, Score: {fila[2]}"
        texto_superficie = font.render(texto, True, "Black")
        screen.blit(texto_superficie, (150, posicion_y))
        posicion_y += 80  
        
def dibujar_score_menu_win(pantalla,font,score):
    string_score_menu_win = f"SCORE FINAL: {str(score)}"
    dibujo_score_menu_win = font.render(string_score_menu_win,True,"Green")
    rect_dibujo_score_menu_win = dibujo_score_menu_win.get_rect()
    rect_dibujo_score_menu_win.center = (640,600)
    pantalla.blit(dibujo_score_menu_win,rect_dibujo_score_menu_win)

def sumar_score(score,score_win,score_extra):
    suma = score_win + score_extra
    score += suma
def calcular_puntos_extras(tiempo_restante):
    if tiempo_restante <60 and tiempo_restante >=50:
        puntos_extras = 250
    elif tiempo_restante <50 and tiempo_restante >=40:
        puntos_extras = 200
    elif tiempo_restante <40 and tiempo_restante >=30:
        puntos_extras = 150
    elif tiempo_restante <30 and tiempo_restante >=20:
        puntos_extras = 100
    elif tiempo_restante <20 and tiempo_restante >=10:
        puntos_extras = 50
    else:
        puntos_extras = 0 

    return puntos_extras


def mostrar_vida_personaje(pantalla,indice):
    lista_vida = ["zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/0_vidas.png","zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/1_vida.png","zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/2_vidas.png","zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/3_vidas.png"]
    imagen_vida = pygame.image.load(lista_vida[indice])
    imagen_vida_reescalada = pygame.transform.scale(imagen_vida,(200,80))
    pantalla.blit(imagen_vida_reescalada,(0,-10))

def fondo_movimiento(pantalla,lista_fondos,contador):
    fondo = pygame.image.load(lista_fondos[contador])
    reescalar_fondo = pygame.transform.scale(fondo,(1280,960))
    pantalla.blit(reescalar_fondo,(0,0))

def actualizar_pantalla(pantalla,personaje: Personaje,fondo,lista_plataformas,lista_plataformas_movil,lista_enemigos,lista_plantas,lista_corazones,piso,posicion_x_flecha,posicion_y_flecha):
    pantalla.blit(fondo,(0,0))
    if len(lista_enemigos) == 0:
        mostrar_flecha_win(pantalla,posicion_x_flecha,posicion_y_flecha)

    piso.blitear_plataforma(pantalla)
    for plataforma in lista_plataformas:
        plataforma.blitear_plataforma(pantalla)

    for corazon in lista_corazones:
        corazon.blitear_corazon(pantalla)
    for enemigo in lista_enemigos:
        enemigo.update(pantalla)
    for planta in lista_plantas:
        planta.update(pantalla)
    for plataforma_movil in lista_plataformas_movil:
        plataforma_movil.update_plataforma_movil(pantalla)
    personaje.update(pantalla)

    if personaje.vida >2 and personaje.vida <=3:
        mostrar_vida_personaje(pantalla,3)
    if personaje.vida >1 and personaje.vida <=2:
        mostrar_vida_personaje(pantalla,2)
    if personaje.vida >0 and personaje.vida <=1:
        mostrar_vida_personaje(pantalla,1)
    if personaje.vida <= 0:
        mostrar_vida_personaje(pantalla,0)

def actualizar_pantalla_final(pantalla,personaje_nave: PersonajeNave,boss: BossFinal,lista_fondos,contador):
    fondo_movimiento(pantalla,lista_fondos,contador)
    personaje_nave.update(pantalla)
    boss.update_boss(pantalla)
    if personaje_nave.vida >2 and personaje_nave.vida <=3:
        mostrar_vida_personaje(pantalla,3)
    if personaje_nave.vida >1 and personaje_nave.vida <=2:
        mostrar_vida_personaje(pantalla,2)
    if personaje_nave.vida >0 and personaje_nave.vida <=1:
        mostrar_vida_personaje(pantalla,1)
    if personaje_nave.vida <= 0:
        mostrar_vida_personaje(pantalla,0)


def creador_nivel(pantalla,lista_plataformas,lista_plataformas_movil,lista_enemigos,lista_plantas,lista_corazones,fondo,piso,personaje:Personaje,posicion_x_flecha,posicion_y_flecha):
    colisionar_enemigo_con_personaje(lista_enemigos,personaje,personaje.lados["left"],personaje.lados["right"],personaje.lados["bottom"])
    colisionar_proyectil_con_enemigo(personaje,lista_enemigos)
    colisionar_enemigo_planta_con_personaje(lista_plantas,personaje,personaje.lados["main"])
    colisionar_proyectil_plataforma(personaje,lista_plataformas)
    colisionar_corazon_con_personaje(lista_corazones,personaje,personaje.lados["main"])
    manejar_colisiones(personaje,piso,lista_plataformas,lista_plataformas_movil)
    actualizar_pantalla(pantalla,personaje,fondo,lista_plataformas,lista_plataformas_movil,lista_enemigos,lista_plantas,lista_corazones,piso,posicion_x_flecha,posicion_y_flecha)


def creador_nivel_final(pantalla,boss,lista_fondos,personaje_nave,contador):
    actualizar_pantalla_final(pantalla,personaje_nave,boss,lista_fondos,contador)
    colisionar_boss_con_personaje(boss,personaje_nave,personaje_nave.lados_nave["left"],personaje_nave.lados_nave["right"],personaje_nave.lados_nave["bottom"],personaje_nave.lados_nave["top"])
    colisionar_proyectil_nave_con_enemigo(personaje_nave,boss)


def pausar_acciones(lista_enemigos,personaje,lista_plataformas_movil):
    for enemigo in lista_enemigos:
        enemigo.velocidad = 0
        enemigo.segundo = 0
        enemigo.velocidad_proyectil = 0
        enemigo.frame = 0
    personaje.frame = 0
    personaje.velocidad_proyectil = 0
    personaje.velocidad = 0
    personaje.esta_pausado = True
    if len(lista_plataformas_movil)>0:
        for plataforma_movil in lista_plataformas_movil:
            plataforma_movil.velocidad = 0
            
def pausar_acciones_boss(personaje_nave,boss_final):
    personaje_nave.frame = 0
    personaje_nave.velocidad_proyectil = 0
    personaje_nave.velocidad = 0
    boss_final.segundo = 0
    boss_final.frame = 0
    boss_final.velocidad_proyectil = 0
    boss_final.velocidad = 0
    boss_final.esta_pausado = True

def despausar_acciones(lista_enemigos,personaje,lista_plataformas_movil):
    for enemigo in lista_enemigos:
        enemigo.velocidad = 5
        enemigo.velocidad_proyectil = 20
        enemigo.frame = 1
        enemigo.segundo = 1

    personaje.frame = 1
    personaje.velocidad_proyectil = 20
    personaje.velocidad = 15
    personaje.esta_pausado = False
    if len(lista_plataformas_movil)>0:
        for plataforma_movil in lista_plataformas_movil:
            plataforma_movil.velocidad = 6

def despausar_acciones_boss(personaje_nave,boss_final):
    personaje_nave.frame = 1
    personaje_nave.velocidad_proyectil = 20
    personaje_nave.velocidad = 25
    boss_final.segundo = 1
    boss_final.frame = 1
    boss_final.velocidad_proyectil = 20
    boss_final.velocidad = 10
    boss_final.esta_pausado = False


def manejar_input_personajes(keys, personaje):
        if keys[pygame.K_RIGHT]:
            personaje.que_hace = "derecha"
        elif keys[pygame.K_LEFT]:
            personaje.que_hace = "izquierda"
        elif keys[pygame.K_UP]:
            if not personaje.esta_agachado:
                personaje.que_hace = "salta"
        elif keys[pygame.K_LCTRL]:
            personaje.que_hace = "agacha"
            personaje.esta_agachado = True
        else:
            if not personaje.esta_disparando:
                personaje.que_hace = "quieto"

        if not keys[pygame.K_LCTRL]:
            personaje.esta_agachado = False

def manejar_input_personaje_nave(keys,personaje_nave):
        if keys[pygame.K_RIGHT]:
            personaje_nave.que_hace = "derecha"
        elif keys[pygame.K_LEFT]:
            personaje_nave.que_hace = "izquierda"
        elif keys[pygame.K_UP]:
            personaje_nave.que_hace = "arriba"
        elif keys[pygame.K_DOWN]:
            personaje_nave.que_hace = "abajo"
        else:
            if not personaje_nave.esta_disparando:
                personaje_nave.que_hace = "quieto"

def manejar_input_disparo_personaje(personaje):
    if not personaje.esta_saltando:
        personaje.que_hace = "dispara"
        personaje.esta_disparando = True

def manejar_input_disparo_personaje_nave(personaje_nave):
    personaje_nave.que_hace = "dispara"
    personaje_nave.esta_disparando = True
def verificar_win(personaje,posicion_y_limite_1,posicion_y_limite_2,lista_enemigos):
    win = False
    if personaje.lados["left"].x >= 1180 :
        if personaje.lados["main"].y >=posicion_y_limite_1 and personaje.lados["main"].y <=posicion_y_limite_2:
            if len(lista_enemigos) == 0:
                win = True

    return win

def verificar_muerto(personaje):
        if personaje.vida <=0:
            return True
def verificar_win_boss_final(boss):
    win = False
    if boss.vida == 0:
        win = True
    return win

