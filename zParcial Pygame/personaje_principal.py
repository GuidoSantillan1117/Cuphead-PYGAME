import pygame
from render_images import *
from proyectil import Proyectil
from personaje_base import PersonajeBaseConProyectiles

class Personaje(PersonajeBaseConProyectiles):
    def __init__(self,animaciones,posicion_inicial_x,posicion_inicial_y) -> None:
        self.vida = 3
        self.daño = 1
        self.contador_pasos = 0
        self.frame = 1
        self.velocidad_proyectil = 20
        self.animaciones = animaciones
        self.reescalar_animaciones()
        
        #gravedad 
        self.gravedad = 1
        self.potencia_salto = -17
        self.limite_velocidad_caida = 25
        self.desplazamiento_y  = 0
        self.velocidad = 15


        self.rectangulo = pygame.Rect(self.animaciones["quieto_derecha"][0].get_rect())
        self.rectangulo.x = posicion_inicial_x
        self.rectangulo.y = posicion_inicial_y

        self.rectangulo_agachado = pygame.Rect(self.animaciones["disparo_agachado_derecha"][0].get_rect())
        self.rectangulo_agachado.x = posicion_inicial_x
        self.rectangulo_agachado.y = posicion_inicial_y+45

        self.imagen_proyectil_derecha = pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/disparo_test_2.png")
        self.imagen_proyectil_izquierda = pygame.transform.flip(self.imagen_proyectil_derecha,True,False)

        self.lados = obtener_rectangulos(self.rectangulo,10)
        self.lados_agachado = obtener_rectangulos(self.rectangulo_agachado,10)


        self.que_hace = "quieto"
        self.ultima_direccion = "derecha"
        self.borde_izquierda = False
        self.borde_derecha = False

        self.esta_saltando = False
        self.esta_disparando = False
        self.esta_agachado = False
        self.presiono_ctrl = False
        self.animacion_disparo = False

        self.colision_izquierda_plataforma = False
        self.colision_derecha_plataforma = False

        self.esta_pausado = False


        self.tiempo_espera_daño = 1  
        self.tiempo_ultimo_daño = 0

        
        self.contador_invulnerabilidad = 0

        self.lista_proyectiles = []

        self.disparo_derecha = False
        self.disparo_izquierda = False

        self.recibe_daño = False

        self.presiono_ctrl = False
        


    def reescalar_animaciones(self):
        lista_reescalar_imagenes = ["derecha","quieto_derecha","izquierda","quieto_izquierda","disparo_derecha","disparo_izquierda"]
        lista_reescalar_imagenes_agachado = ["agachado_derecha","agachado_izquierda","disparo_agachado_derecha","disparo_agachado_izquierda"]
        for clave in self.animaciones:
            if clave in lista_reescalar_imagenes:
                reescalar_imagen(self.animaciones[clave],(98,145)) 
            if clave in lista_reescalar_imagenes_agachado:
                reescalar_imagen(self.animaciones[clave],(98,110)) 


    def animar(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        if not self.esta_agachado:
            pantalla.blit(animacion[self.contador_pasos],self.lados["main"])
        else:
            pantalla.blit(animacion[self.contador_pasos],self.lados_agachado["main"])
        self.contador_pasos += self.frame

    def animar_daño(self,pantalla,accion):
        self.animar(pantalla,accion)
        self.recibe_daño = False

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
        for lado_agachado in self.lados_agachado:
            self.lados_agachado[lado_agachado].x += velocidad
        if self.lados["left"].x <5:
            self.borde_izquierda = True
        elif self.lados["left"].x >5:
            self.borde_izquierda = False

        if self.lados["right"].x >1270:
            self.borde_derecha = True
        elif self.lados["right"].x <1270:
            self.borde_derecha = False


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
                    if not self.esta_agachado:
                        self.crear_proyectil(self.lados["main"].right+5,self.lados["main"].y+50,velocidad,self.lista_proyectiles)
                    elif self.esta_agachado:
                        self.crear_proyectil(self.lados["main"].right+5,self.lados_agachado["main"].y+50,velocidad,self.lista_proyectiles)
                        
                case "izquierda":
                    if not self.esta_agachado:
                        self.crear_proyectil(self.lados["main"].left-60,self.lados["main"].y+50,velocidad,self.lista_proyectiles)
                    elif self.esta_agachado:
                        self.crear_proyectil(self.lados["main"].left-60,self.lados_agachado["main"].y+50,velocidad,self.lista_proyectiles)

        self.animacion_disparo = False


    def update_proyectiles(self, pantalla, velocidad):
        self.agregar_proyectiles_lista(velocidad)
        super().dibujar_listas_proyectiles(pantalla, self.lista_proyectiles, velocidad)

    def verificar_colision_proyectil(self, lista, rectangulo_izquierda, rectangulo_derecha):
        return super().verificar_colision_proyectil(lista, rectangulo_izquierda, rectangulo_derecha)


    def dañar(self,vida_enemigo):
        dañado = vida_enemigo - self.daño
        return dañado

    def esta_muerto(self):
        return self.vida <= 0

    def aplicar_gravedad(self,pantalla):
        if self.esta_saltando:
            if self.ultima_direccion == "derecha":
                self.animar(pantalla,"salta_derecha")
                if self.recibe_daño:
                    self.animar_daño(pantalla,"recibe_daño_salta_derecha")
            elif self.ultima_direccion == "izquierda":
                self.animar(pantalla,"salta_izquierda")
                if self.recibe_daño:
                    self.animar_daño(pantalla,"recibe_daño_salta_izquierda")

            if not self.esta_pausado:
                for lado in self.lados:
                    self.lados[lado].y += self.desplazamiento_y
                for lado_agachado in self.lados_agachado:
                    self.lados_agachado[lado_agachado].y += self.desplazamiento_y
                if self.desplazamiento_y + self.gravedad<self.limite_velocidad_caida:
                    self.desplazamiento_y += self.gravedad
                if self.lados["top"].y  <=5:
                    self.desplazamiento_y = 2

    def update(self,pantalla):
        match self.que_hace:
            case "derecha":
                self.ultima_direccion = "derecha"
                if not self.esta_saltando and not self.esta_agachado:
                    self.animar(pantalla,"derecha")
                    if self.recibe_daño:
                        self.animar_daño(pantalla,"recibe_daño_derecha")
                if not self.borde_derecha and not self.colision_izquierda_plataforma:
                    self.mover(self.velocidad)
                if not self.esta_saltando and self.esta_agachado:
                    self.animar(pantalla,"agachado_derecha")
                    if self.recibe_daño:
                        self.animar_daño(pantalla,"recibe_daño_agachado_derecha")

            case "izquierda":
                self.ultima_direccion = "izquierda"
                if not self.esta_saltando and not self.esta_agachado:
                    self.animar(pantalla,"izquierda")
                    if self.recibe_daño:
                        self.animar_daño(pantalla,"recibe_daño_izquierda")
                if not self.borde_izquierda and not self.colision_derecha_plataforma:
                    self.mover(self.velocidad *-1)
                if not self.esta_saltando and self.esta_agachado:
                    self.animar(pantalla,"agachado_izquierda")
                    if self.recibe_daño:
                        self.animar_daño(pantalla,"recibe_daño_agachado_izquierda")

            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto

            case "dispara":
                if self.ultima_direccion == "derecha" and not self.esta_agachado:
                    self.animar(pantalla,"disparo_derecha") 
                if self.ultima_direccion == "izquierda" and not self.esta_agachado:
                    self.animar(pantalla,"disparo_izquierda")
                if self.ultima_direccion == "derecha" and self.esta_agachado:
                    self.animar(pantalla,"disparo_agachado_derecha")
                if self.ultima_direccion == "izquierda" and self.esta_agachado:
                    self.animar(pantalla,"disparo_agachado_izquierda")

                self.animacion_disparo = True
                self.esta_disparando = False
            case "quieto":
                if not self.animacion_disparo:
                    if not self.esta_saltando:
                        if self.ultima_direccion == "derecha":
                            if not self.esta_agachado:
                                self.animar(pantalla,"quieto_derecha")
                            if self.recibe_daño:
                                self.animar_daño(pantalla,"recibe_daño_quieto_derecha")
                            if self.esta_agachado:
                                self.animar(pantalla,"agachado_derecha")
                        elif self.ultima_direccion == "izquierda":
                            if not self.esta_agachado:
                                self.animar(pantalla,"quieto_izquierda")
                            if self.recibe_daño:
                                self.animar_daño(pantalla,"recibe_daño_quieto_izquierda")
                            if self.esta_agachado:
                                self.animar(pantalla,"agachado_izquierda")
            case "agacha":
                if not self.esta_saltando:
                    if self.ultima_direccion == "derecha":
                        self.animar(pantalla,"agachado_derecha")
                    elif self.ultima_direccion == "izquierda":
                        self.animar(pantalla,"agachado_izquierda")


        self.aplicar_gravedad(pantalla)

        if self.colision_izquierda_plataforma:
            self.colision_izquierda_plataforma = False

        if self.colision_derecha_plataforma:
            self.colision_derecha_plataforma = False
        self.update_proyectiles(pantalla,self.velocidad_proyectil)

