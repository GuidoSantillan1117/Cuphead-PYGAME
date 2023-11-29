import pygame
from proyectil import *
from render_images import *
class Enemigos:
    def __init__(self,posicion_x,posicion_y,diccionario_animaciones,enemigo_tirador:bool,borde_izquierda_plataforma,borde_derecha_plataforma,direccion_apuntado,delay_disparo,vida) -> None:
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.animaciones_enemigos = diccionario_animaciones
        self.reescalar_animaciones(enemigo_tirador)
        self.vida_enemigo = vida

        self.rectangulo_enemigo = pygame.Rect(self.animaciones_enemigos["derecha"][1].get_rect())
        self.rectangulo_enemigo.x = posicion_x
        self.rectangulo_enemigo.y = posicion_y

        self.imagen_proyectil_derecha = pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_tirador/lobber_seed_0007.png")
        self.imagen_proyectil_izquierda = pygame.transform.flip(self.imagen_proyectil_derecha,True,False)

        self.lados_enemigo = obtener_rectangulos(self.rectangulo_enemigo,10)
        self.direccion = "izquierda"
        self.contador_pasos = 0
        self.frame = 1

        self.velocidad = 5
        self.velocidad_proyectil = 20
        self.tipo_enemigo_tirador = enemigo_tirador
        self.animacion_disparo = False

        self.alcanzo_borde_izquierda = False
        self.alcanzo_borde_derecha = False

        self.borde_izquierda_plataforma = borde_izquierda_plataforma
        self.borde_derecha_plataforma = borde_derecha_plataforma

        self.timer_disparo = 0
        self.segundo = 1
        self.delay = delay_disparo
        self.lista_proyectiles_enemigo = []
        self.direccion_apuntado = direccion_apuntado
        self.enemigo_disparo = False


        self.recibe_daño = False


    def reescalar_animaciones(self,enemigo_tirador):
        for clave in self.animaciones_enemigos:
            if enemigo_tirador:
                reescalar_imagen(self.animaciones_enemigos[clave],(70,70)) #100 110
            if not enemigo_tirador:
                reescalar_imagen(self.animaciones_enemigos[clave],(110,110))
                

    def animar(self,pantalla,que_animacion):
        animacion = self.animaciones_enemigos[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos],self.lados_enemigo["main"])
        self.contador_pasos += self.frame

    def mover(self,velocidad,borde_izquierda_plataforma,borde_derecha_plataforma):
        if borde_izquierda_plataforma != 0 and borde_derecha_plataforma != 0:
            if not self.tipo_enemigo_tirador:
                if self.vida_enemigo >0:
                    for lado in self.lados_enemigo:
                        self.lados_enemigo[lado].x+=velocidad
                    
                    if self.direccion == "izquierda":
                        if self.lados_enemigo["left"].x <= borde_izquierda_plataforma:
                            self.alcanzo_borde_izquierda = True
                        if self.alcanzo_borde_derecha:
                            self.alcanzo_borde_derecha = False

                    elif self.direccion == "derecha":
                        if self.lados_enemigo["right"].x >= borde_derecha_plataforma:
                            self.alcanzo_borde_derecha = True
                        if self.alcanzo_borde_izquierda:
                            self.alcanzo_borde_izquierda = False

    def verificar_colision_enemigo_con_personaje(self,rect_izquierda,rect_derecha,rect_bottom):
        colisiono = False
        if self.lados_enemigo["left"].colliderect(rect_derecha) or self.lados_enemigo["right"].colliderect(rect_izquierda) or self.lados_enemigo["top"].colliderect(rect_bottom):
            colisiono = True

        return colisiono

    def dañar(self,vida_personaje,daño):
        dañado = vida_personaje - daño
        return dañado

    def crear_proyectil_enemigo(self,velocidad,direccion_apuntado):
        if self.tipo_enemigo_tirador and self.timer_disparo == self.delay:
            if direccion_apuntado == 1:
                proyectil_enemigo = Proyectil(self.lados_enemigo["main"].right,self.lados_enemigo["main"].y+20,velocidad,1,self.imagen_proyectil_derecha,(40,40))
            if direccion_apuntado == -1:
                proyectil_enemigo = Proyectil(self.lados_enemigo["main"].left,self.lados_enemigo["main"].y+20,velocidad,-1,self.imagen_proyectil_izquierda,(40,40))
            self.enemigo_disparo = True
            self.lista_proyectiles_enemigo.append(proyectil_enemigo)
            self.timer_disparo = 0

    def dibujar_listas_proyectiles (self,pantalla,lista,velocidad):     
        for proyectil in lista:
            proyectil.animar_proyectil(pantalla)
            proyectil.trayecto_proyectil(velocidad)

    def update_proyectiles(self,pantalla,velocidad,direccion_apuntado):
        if self.vida_enemigo >0:
            self.crear_proyectil_enemigo(velocidad,direccion_apuntado)
            self.dibujar_listas_proyectiles(pantalla,self.lista_proyectiles_enemigo,velocidad)

    

    def verificar_colision_proyectil_enemigo_con_jugador(self,rectangulo_izquierda,rectangulo_derecha):
        colisiono = False
        for proyectil in self.lista_proyectiles_enemigo:
            if proyectil.lados_proyectil["main"].colliderect(rectangulo_izquierda) or proyectil.lados_proyectil["main"].colliderect(rectangulo_derecha):
                self.lista_proyectiles_enemigo.remove(proyectil)
                colisiono = True
        return colisiono


    def animar_daño(self,pantalla,accion):
        self.animar(pantalla,accion)
        self.recibe_daño = False

    def update(self,pantalla):
        if not self.tipo_enemigo_tirador:
            match self.direccion:
                case "izquierda":
                        self.animar(pantalla,"derecha")
                        if self.recibe_daño:
                            self.animar_daño(pantalla,"derecha_dañado")
                        self.mover(self.velocidad*-1,self.borde_izquierda_plataforma,self.borde_derecha_plataforma)
                case "derecha":
                        self.animar(pantalla,"izquierda")
                        if self.recibe_daño:
                            self.animar_daño(pantalla,"izquierda_dañado")
                        self.mover(self.velocidad,self.borde_izquierda_plataforma,self.borde_derecha_plataforma)

            if self.alcanzo_borde_izquierda:
                self.direccion = "derecha"
            elif self.alcanzo_borde_derecha:
                self.direccion = "izquierda"

                
        self.timer_disparo += self.segundo 
        if self.tipo_enemigo_tirador and self.direccion_apuntado == -1:
            self.animar(pantalla,"izquierda")
            if self.recibe_daño:
                self.animar_daño(pantalla,"izquierda_dañado")

        if self.tipo_enemigo_tirador and self.direccion_apuntado == 1:
            self.animar(pantalla,"derecha")
            if self.recibe_daño:
                self.animar_daño(pantalla,"derecha_dañado")

        self.update_proyectiles(pantalla,self.velocidad_proyectil,self.direccion_apuntado)


    