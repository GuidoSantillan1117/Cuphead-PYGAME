from modo_admin import *
import pygame
def hitbox_nivel_1(pantalla,personaje,lista_plataformas,lista_enemigos):
    if get_modo():
        pintar_hitbox_personaje(pantalla,personaje)
        pintar_hitbox_plataforma(pantalla,lista_plataformas)
        pintar_hitbox_enemigos(pantalla,lista_enemigos)

def hitbox_nivel_2(pantalla,personaje,lista_plataformas,lista_plataformas_movil,lista_enemigos,lista_enemigos_planta):
    if get_modo():
        pintar_hitbox_personaje(pantalla,personaje)
        pintar_hitbox_plataforma(pantalla,lista_plataformas)
        pintar_hitbox_plataforma_movil(pantalla,lista_plataformas_movil)
        pintar_hitbox_enemigos(pantalla,lista_enemigos)
        pintar_hitbox_enemigos_planta(pantalla,lista_enemigos_planta)

def hitbox_nivel_3(pantalla,personaje_nave,boss_final):
    if get_modo():
        pintar_hitbox_personaje_nave(pantalla,personaje_nave)
        pintar_hitbox_boss(pantalla,boss_final)


def pintar_hitbox_personaje(pantalla,personaje):
    for lado in personaje.lados:
        pygame.draw.rect(pantalla,"Green",personaje.lados[lado],3)
    for lado in personaje.lados_agachado:
        pygame.draw.rect(pantalla,"Yellow",personaje.lados_agachado[lado],3)
def pintar_hitbox_personaje_nave(pantalla,personaje_nave):
    for lado in personaje_nave.lados_nave:
        pygame.draw.rect(pantalla,"Green",personaje_nave.lados_nave[lado],3)

def pintar_hitbox_plataforma(pantalla,lista_plataformas):
    for plataforma in lista_plataformas:
        for lado in plataforma.lados_plataforma:
            pygame.draw.rect(pantalla,"Black",plataforma.lados_plataforma[lado],3)

def pintar_hitbox_plataforma_movil(pantalla,lista_plataformas_movil):
    for plataforma_movil in lista_plataformas_movil:
        for lado in plataforma_movil.lados_plataforma:
            pygame.draw.rect(pantalla,"Grey",plataforma_movil.lados_plataforma[lado],3)


def pintar_hitbox_enemigos(pantalla,lista_enemigos):
    for enemigo in lista_enemigos:
        for lado in enemigo.lados_enemigo:
            pygame.draw.rect(pantalla,"Red",enemigo.lados_enemigo[lado],3)

def pintar_hitbox_enemigos_planta(pantalla,lista_enemigos_planta):
    for enemigo_planta in lista_enemigos_planta:
        for lado in enemigo_planta.lados_planta:
            pygame.draw.rect(pantalla,"Red",enemigo_planta.lados_planta[lado],3)
def pintar_hitbox_boss(pantalla,boss):
    for lado in boss.lados:
        pygame.draw.rect(pantalla,"Red",boss.lados[lado],3)




