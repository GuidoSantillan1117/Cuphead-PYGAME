from plataformas import Plataforma
from render_images import *
import pygame

class PlataformaMovil():
    def __init__(self, path_imagen, posicion_x, posicion_y, tamaño,limite_left,limite_right):
        self.imagen_plataforma_movil = pygame.image.load(path_imagen)
        self.imagen_plataforma_movil = self.reescalar(self.imagen_plataforma_movil,tamaño) 
        self.rectangulo_plataforma_movil = pygame.Rect(self.imagen_plataforma_movil.get_rect())
        self.rectangulo_plataforma_movil.x = posicion_x
        self.rectangulo_plataforma_movil.y = posicion_y

        self.lados_plataforma = obtener_rectangulos_plataforma(self.rectangulo_plataforma_movil)

        self.movimiento_activado = True
        self.velocidad = 6
        self.direccion = "derecha"

        self.limite_left = limite_left
        self.limite_right = limite_right
        self.alcanzo_limite_derecha = False
        self.alcanzo_limite_izquierda = False

    def reescalar(self, imagen,tamaño):
        return pygame.transform.scale(imagen, (tamaño))

    def mover(self,velocidad,limite_left,limite_right):
        if self.movimiento_activado:
            for lado in self.lados_plataforma:
                self.lados_plataforma[lado].x += velocidad
                if self.direccion == "izquierda":
                    if self.lados_plataforma["left"].x <= limite_left:
                        self.alcanzo_limite_izquierda = True
                        
                    if self.alcanzo_limite_derecha:
                        self.alcanzo_limite_derecha = False

                elif self.direccion == "derecha":
                    if self.lados_plataforma["right"].x >= limite_right:
                        self.alcanzo_limite_derecha = True
                    if self.alcanzo_limite_izquierda:
                        self.alcanzo_limite_izquierda = False


    def blitear_plataforma_movil(self, pantalla):
        pantalla.blit(self.imagen_plataforma_movil,self.lados_plataforma["main"])

    def update_plataforma_movil(self,pantalla):
        match self.direccion:
                case "izquierda":
                    self.mover(self.velocidad*-1,self.limite_left,self.limite_right)
                case "derecha":
                    self.mover(self.velocidad,self.limite_left,self.limite_right)
        if self.alcanzo_limite_izquierda:
            self.direccion = "derecha"
        elif self.alcanzo_limite_derecha:
            self.direccion = "izquierda"

        self.blitear_plataforma_movil(pantalla)          


