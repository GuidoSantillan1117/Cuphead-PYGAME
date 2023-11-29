import pygame
from render_images import *
class PlantaCarnivora:
    def __init__(self,posicion_x,posicion_y,animaciones,tamaño) -> None:
        self.animaciones = animaciones
        self.reescalar_animaciones(tamaño)
        self.rectangulo_planta = pygame.Rect(self.animaciones["quieto"][0].get_rect())
        self.rectangulo_planta.x = posicion_x
        self.rectangulo_planta.y = posicion_y

        self.ataque = False
        self.contador_frames = 0

        self.lados_planta = obtener_rectangulos(self.rectangulo_planta,10)


    def reescalar_animaciones(self,tamaño):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave],(tamaño))
            
    def verificar_colision_planta(self,rect_main):
        colisiono = False
        if self.lados_planta["main"].colliderect(rect_main):
            colisiono = True

        return colisiono
    
    def dañar(self,vida_personaje):
        dañado = vida_personaje - 3
        return dañado

    def animar(self,pantalla,que_animacion):
        animacion = self.animaciones[que_animacion]
        if self.ataque:
            self.contador_frames += 1
            if self.contador_frames >2:
                self.contador_frames = 2
        elif not self.ataque:
            self.contador_frames = 0
        pantalla.blit(animacion[self.contador_frames],self.lados_planta["main"])

    def update(self,pantalla):
        if not self.ataque:
            self.animar(pantalla,"quieto")

        if self.ataque:
            self.animar(pantalla,"ataca")



