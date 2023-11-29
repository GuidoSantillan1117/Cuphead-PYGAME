import pygame
from render_images import *
from personaje_base import PersonajeBaseConProyectiles
from proyectil import Proyectil
class PersonajeNave(PersonajeBaseConProyectiles):
    def __init__(self,posicion_x,posicion_y,animaciones) -> None:
        self.vida = 3
        self.daño = 2
        self.velocidad = 25
        self.contador_frames = 0
        self.frame = 1
        self.animaciones = animaciones
        self.reescalar_animaciones()
        
        self.rectangulo_nave = pygame.Rect(self.animaciones["derecha"][0].get_rect())
        self.rectangulo_nave.x = posicion_x
        self.rectangulo_nave.y = posicion_y

        self.borde_izquierda = False
        self.borde_derecha = False
        self.borde_arriba = False
        self.borde_abajo = False

        self.imagen_proyectil_derecha = pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_nave/tiro_nave.png") 
        self.imagen_proyectil_izquierda = pygame.transform.flip(self.imagen_proyectil_derecha,True,False)

        self.ultima_direccion = "derecha"
        self.que_hace = "quieto"
        self.esta_disparando = False
        self.animacion_disparo = False
        self.velocidad_proyectil = 20

        self.tiempo_espera_daño = 1  
        self.tiempo_ultimo_daño = 0


        self.lados_nave = obtener_rectangulos(self.rectangulo_nave,10)
        self.lista_proyectiles = []

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave],(98,145))

    def animar(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_frames >= largo:
            self.contador_frames = 0

        pantalla.blit(animacion[self.contador_frames],self.lados_nave["main"])

        self.contador_frames +=self.frame

    def mover_x(self,velocidad):
        for lado in self.lados_nave:
            self.lados_nave[lado].x += velocidad

        if self.lados_nave["right"].x >1270:
            self.borde_derecha = True
        elif self.lados_nave["right"].x <1270:
            self.borde_derecha = False

        if self.lados_nave["left"].x <5:
            self.borde_izquierda = True
        elif self.lados_nave["left"].x >5:
            self.borde_izquierda = False

    def mover_y(self,velocidad):
        for lado in self.lados_nave:
            self.lados_nave[lado].y += velocidad

        if self.lados_nave["top"].y <10:
            self.borde_arriba = True
        elif self.lados_nave["top"].y >10:
            self.borde_arriba = False

        if self.lados_nave["bottom"].y >950:
            self.borde_abajo = True
        elif self.lados_nave["bottom"].y <950:
            self.borde_abajo = False
    
    def crear_proyectil(self,posicion_x,posicion_y,velocidad,lista):
        if self.ultima_direccion == "derecha":
            nuevo_proyectil = Proyectil(posicion_x,posicion_y,velocidad,1,self.imagen_proyectil_derecha,(80,40))
        if self.ultima_direccion == "izquierda":
            nuevo_proyectil = Proyectil(posicion_x,posicion_y,velocidad,-1,self.imagen_proyectil_izquierda,(80,40))
        lista.append(nuevo_proyectil)


    def agregar_proyectiles_lista(self,velocidad):
        if self.animacion_disparo:
            match self.ultima_direccion:
                case "derecha":
                        self.crear_proyectil(self.lados_nave["main"].right+5,self.lados_nave["main"].y+50,velocidad,self.lista_proyectiles)
                        
                case "izquierda":
                        self.crear_proyectil(self.lados_nave["main"].left-80,self.lados_nave["main"].y+50,velocidad,self.lista_proyectiles)
        self.animacion_disparo = False

                
    def update_proyectiles(self, pantalla, velocidad):
        self.agregar_proyectiles_lista(velocidad)
        super().dibujar_listas_proyectiles(pantalla, self.lista_proyectiles, velocidad)

    def verificar_colision_proyectil(self, lista, rectangulo_izquierda, rectangulo_derecha):
        return super().verificar_colision_proyectil(lista, rectangulo_izquierda, rectangulo_derecha)


    
    def dañar(self,vida_enemigo):
        dañado = vida_enemigo - self.daño
        return dañado

    def update(self,pantalla):
        match self.que_hace:
            case "quieto":
                if self.ultima_direccion == "derecha":
                    self.animar(pantalla,"derecha")
                if self.ultima_direccion == "izquierda":
                    self.animar(pantalla,"izquierda")
            case "derecha":
                self.ultima_direccion = "derecha"
                if not self.borde_derecha:
                    self.mover_x(self.velocidad)
                self.animar(pantalla,"derecha")
            case "izquierda":
                self.ultima_direccion = "izquierda"
                if not self.borde_izquierda:
                    self.mover_x(self.velocidad*-1)
                self.animar(pantalla,"izquierda")
            case "arriba":
                if not self.borde_arriba:
                    self.mover_y(self.velocidad*-1)
                if self.ultima_direccion == "derecha":
                    self.animar(pantalla,"derecha")
                if self.ultima_direccion == "izquierda":
                    self.animar(pantalla,"izquierda")
            case "abajo":
                if not self.borde_abajo:
                    self.mover_y(self.velocidad)
                if self.ultima_direccion == "derecha":
                    self.animar(pantalla,"derecha")
                if self.ultima_direccion == "izquierda":
                    self.animar(pantalla,"izquierda")

            
            case "dispara":
                if self.ultima_direccion == "derecha":
                    self.animar(pantalla,"derecha") 
                if self.ultima_direccion == "izquierda":
                    self.animar(pantalla,"izquierda")

                self.animacion_disparo = True
                self.esta_disparando = False
        self.update_proyectiles(pantalla,self.velocidad_proyectil)