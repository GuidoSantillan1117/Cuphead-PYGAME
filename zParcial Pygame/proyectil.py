import pygame
from personaje_principal import *
class Proyectil:
    def __init__(self,posicion_x,posicion_y,velocidad,direccion,imagen,tamaño) -> None:
        self.imagen_proyectil = self.reescalar(imagen,tamaño)
        self.daño = 10
        self.velocidad = velocidad
        self.direccion = direccion

        self.rectangulo_proyectil = pygame.Rect(self.imagen_proyectil.get_rect())
        self.rectangulo_proyectil.x = posicion_x
        self.rectangulo_proyectil.y = posicion_y
        self.lados_proyectil = obtener_rectangulos(self.rectangulo_proyectil,5)

        self.proyectil_derecha = False
        self.proyectil_izquierda = False

    def reescalar(self, imagen,tamaño):
        return pygame.transform.scale(imagen, (tamaño)) 
        
    def trayecto_proyectil(self,velocidad):  
        for lado in self.lados_proyectil:
            self.lados_proyectil[lado].x += velocidad * self.direccion

    def trayecto_proyectil_y(self,velocidad):
        for lado in self.lados_proyectil:
            self.lados_proyectil[lado].y += velocidad

    def animar_proyectil(self,pantalla):
        pantalla.blit(self.imagen_proyectil,self.rectangulo_proyectil)
