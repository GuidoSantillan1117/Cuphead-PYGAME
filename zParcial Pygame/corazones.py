import pygame
class Corazones():
    def __init__(self,posicion_x,posicion_y) -> None:
        self.imagen_corazon = pygame.image.load("zParcial Pygame/imagenes_cuphead/plataformas/corazon.png")
        self.imagen_corazon = self.reescalar(self.imagen_corazon,(60,40))
        self.rectangulo_corazon = pygame.Rect(self.imagen_corazon.get_rect())
        self.rectangulo_corazon.x = posicion_x
        self.rectangulo_corazon.y = posicion_y

    def curar(self,vida_personaje):
        if vida_personaje <3:
            curar = vida_personaje + 1
        return curar

    def reescalar(self, imagen,tamaño):
        return pygame.transform.scale(imagen, (tamaño))

    def verificar_colision_corazon(self,rectangulo_personaje,vida_personaje):
        colisiono = False
        if self.rectangulo_corazon.colliderect(rectangulo_personaje) and vida_personaje <3:
            colisiono = True
        return colisiono

    def blitear_corazon(self, pantalla):
        pantalla.blit(self.imagen_corazon, self.rectangulo_corazon)