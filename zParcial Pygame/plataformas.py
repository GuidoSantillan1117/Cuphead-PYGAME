import pygame
from render_images import *
class Plataforma:
    def __init__(self,path_imagen,posicion_x, posicion_y,tamaño,tronco =False):
        self.imagen_plataforma = pygame.image.load(path_imagen)
        self.imagen_plataforma = self.reescalar(self.imagen_plataforma,tamaño) 
        self.rectangulo_plataforma = pygame.Rect(self.imagen_plataforma.get_rect())
        self.rectangulo_plataforma.x = posicion_x
        self.rectangulo_plataforma.y = posicion_y
        self.es_tronco = tronco

        self.lados_plataforma = obtener_rectangulos_plataforma(self.rectangulo_plataforma)

    def reescalar(self, imagen,tamaño):
        return pygame.transform.scale(imagen, (tamaño))

    def blitear_plataforma(self, pantalla):
        pantalla.blit(self.imagen_plataforma, self.rectangulo_plataforma)

