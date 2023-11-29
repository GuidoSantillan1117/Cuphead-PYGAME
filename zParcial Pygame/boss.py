import pygame
from render_images import *
from proyectil import Proyectil
class BossFinal:
    def __init__(self,animaciones) -> None:
        self.vida = 10
        self.daño = 3
        self.velocidad = 10
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.rectangulo_boss = pygame.Rect(self.animaciones["izquierda"][0].get_rect())
        self.rectangulo_boss.x = 800
        self.rectangulo_boss.y = 500

        self.borde_arriba = 50
        self.borde_abajo = 910
        self.lados = obtener_rectangulos(self.rectangulo_boss,20)

        self.alcanzo_borde_arriba = False
        self.alcanzo_borde_abajo = False
        self.alcanzo_borde_izquierda = False
        self.alcanzo_borde_derecha = False


        self.imagen_proyectil_izquierda = pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/bird_mad_flap_feather_pink_0003.png")
        self.imagen_proyectil_derecha = pygame.transform.flip(self.imagen_proyectil_izquierda,True,False)
        self.disparo_arriba = False
        self.timer_disparo = 0
        self.velocidad_proyectil = 20

        self.contador_frames = 0
        self.frame = 1
        self.segundo = 1
        self.inmunidad = False
        self.esta_pausado = False
        self.esta_dañado = False


        self.contador = 0

        self.direccion = "arriba"
        self.direccion_apuntado = "izquierda"
        self.ataque_normal = False
        self.ataque_arriba = False



        self.lista_proyectiles_boss = []
        

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave],(450,400))

    def movimiento_boss(self,velocidad):
        if self.vida >0:
            for lado in self.lados:
                self.lados[lado].y += velocidad

            if self.direccion == "arriba":
                if self.lados["top"].y <= self.borde_arriba:
                    self.alcanzo_borde_arriba = True

                if self.alcanzo_borde_abajo:
                    self.alcanzo_borde_abajo = False

            if self.direccion == "abajo":
                if self.lados["bottom"].y >= self.borde_abajo:
                    self.alcanzo_borde_abajo = True

                if self.alcanzo_borde_arriba:
                    self.alcanzo_borde_arriba = False
            
        
    def mover_boss_izquierda(self):
        for lado in self.lados:
            if not self.alcanzo_borde_izquierda:
                self.inmunidad = True
                self.lados[lado].x -= 10
            
            if self.lados["left"].x <=20:
                self.inmunidad = False
                self.alcanzo_borde_izquierda = True
                self.direccion_apuntado = "derecha"

    def mover_boss_derecha_disparo_arriba(self):
        self.alcanzo_borde_izquierda = False
        for lado in self.lados:
            if not self.alcanzo_borde_derecha:
                self.inmunidad = True
                self.lados[lado].x += 10

            if self.lados["right"].x >=1250:
                self.inmunidad = False
                self.disparo_arriba = True
                self.alcanzo_borde_derecha = True
                self.direccion_apuntado = "izquierda"

    def mover_boss_izquierda_disparo_arriba(self):
        for lado in self.lados:
            if not self.alcanzo_borde_izquierda:
                self.inmunidad = True
                self.lados[lado].x -= 10

            if self.lados["left"].x <=20:
                self.inmunidad = False
                self.disparo_arriba = True
                self.alcanzo_borde_izquierda = True
                self.direccion_apuntado = "derecha"

    def tpear_boss(self):
        if not self.esta_pausado:
            if self.vida >40 and self.vida<=60:
                self.mover_boss_izquierda()
            if self.vida >20 and self.vida<=40:
                self.mover_boss_derecha_disparo_arriba()
            if self.vida >0 and self.vida <20:
                self.mover_boss_izquierda_disparo_arriba()


    def animar(self,pantalla,que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_frames >= largo:
            self.contador_frames = 0
        pantalla.blit(animacion[self.contador_frames],self.lados["main"])
        self.contador_frames +=self.frame

    def update_boss(self,pantalla):

        if self.direccion == "arriba":
                self.movimiento_boss(self.velocidad*-1)
                if self.direccion_apuntado == "izquierda":
                    self.animar(pantalla,"izquierda")
                elif self.direccion_apuntado == "derecha":
                    self.animar(pantalla,"derecha")
        if self.direccion == "abajo":
                self.movimiento_boss(self.velocidad)
                if self.direccion_apuntado == "izquierda":
                    self.animar(pantalla,"izquierda")
                elif self.direccion_apuntado == "derecha":
                    self.animar(pantalla,"derecha")
        if self.direccion_apuntado == "derecha" and self.esta_dañado:
                self.animar(pantalla,"derecha_dañado")
                self.esta_dañado = False
        if self.direccion_apuntado == "izquierda" and self.esta_dañado:
                self.animar(pantalla,"izquierda_dañado")
                self.esta_dañado = False

                    

        self.tpear_boss()

        if self.alcanzo_borde_arriba:
            self.direccion = "abajo"
        if self.alcanzo_borde_abajo:
            self.direccion = "arriba"

        self.timer_disparo +=self.segundo
        self.update_proyectiles(pantalla,self.velocidad_proyectil)


    def verificar_colision_boss_con_personaje(self,rect_izquierda,rect_derecha,rect_bottom,rect_top):
        colisiono = False
        if self.lados["left"].colliderect(rect_derecha) or self.lados["right"].colliderect(rect_izquierda) or self.lados["top"].colliderect(rect_bottom) or self.lados["bottom"].colliderect(rect_top):
            colisiono = True
        return colisiono

    def dañar(self,vida_personaje,daño):
        dañado = vida_personaje - daño
        return dañado

    def crear_proyectil_enemigo(self,velocidad):
        if self.timer_disparo == 40:
            if not self.disparo_arriba:
                self.ataque_normal = True
                if self.direccion_apuntado == "derecha":
                        proyectil_boss_1 = Proyectil(self.lados["main"].right,self.lados["main"].y+40,velocidad,1,self.imagen_proyectil_derecha,(100,60))
                        proyectil_boss_2 = Proyectil(self.lados["main"].right,self.lados["main"].y+140,velocidad,1,self.imagen_proyectil_derecha,(100,60))
                        proyectil_boss_3 = Proyectil(self.lados["main"].right,self.lados["main"].y+240,velocidad,1,self.imagen_proyectil_derecha,(100,60))
                        
                        self.lista_proyectiles_boss.append(proyectil_boss_1)
                        self.lista_proyectiles_boss.append(proyectil_boss_2)
                        self.lista_proyectiles_boss.append(proyectil_boss_3)

                if self.direccion_apuntado == "izquierda":
                    proyectil_boss_1 = Proyectil(self.lados["main"].left,self.lados["main"].y+40,velocidad,-1,self.imagen_proyectil_izquierda,(100,60))
                    proyectil_boss_2 = Proyectil(self.lados["main"].left,self.lados["main"].y+140,velocidad,-1,self.imagen_proyectil_izquierda,(100,60))
                    proyectil_boss_3 = Proyectil(self.lados["main"].left,self.lados["main"].y+240,velocidad,-1,self.imagen_proyectil_izquierda,(100,60))
                    self.lista_proyectiles_boss.append(proyectil_boss_1)
                    self.lista_proyectiles_boss.append(proyectil_boss_2)
                    self.lista_proyectiles_boss.append(proyectil_boss_3)

            if self.disparo_arriba:
                self.ataque_arriba = True
                self.contador +=1
                if self.contador == 1:
                    proyectil_boss_1 = Proyectil(100,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_2 = Proyectil(300,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_3 = Proyectil(500,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_4 = Proyectil(700,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_5 = Proyectil(900,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_6 = Proyectil(1100,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))

                    self.lista_proyectiles_boss.append(proyectil_boss_1)
                    self.lista_proyectiles_boss.append(proyectil_boss_2)
                    self.lista_proyectiles_boss.append(proyectil_boss_3)
                    self.lista_proyectiles_boss.append(proyectil_boss_4)
                    self.lista_proyectiles_boss.append(proyectil_boss_5)
                    self.lista_proyectiles_boss.append(proyectil_boss_6)

                if self.contador == 2:
                    proyectil_boss_1 = Proyectil(200,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_2 = Proyectil(400,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_3 = Proyectil(600,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_4 = Proyectil(800,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_5 = Proyectil(1000,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))
                    proyectil_boss_6 = Proyectil(1200,-20,velocidad,-1,self.imagen_proyectil_izquierda,(60,40))

                    self.lista_proyectiles_boss.append(proyectil_boss_1)
                    self.lista_proyectiles_boss.append(proyectil_boss_2)
                    self.lista_proyectiles_boss.append(proyectil_boss_3)
                    self.lista_proyectiles_boss.append(proyectil_boss_4)
                    self.lista_proyectiles_boss.append(proyectil_boss_5)
                    self.lista_proyectiles_boss.append(proyectil_boss_6)
                    self.contador = 0


            self.timer_disparo = 0
            

    def dibujar_listas_proyectiles (self,pantalla,lista,velocidad):     
        for proyectil in lista:
            proyectil.animar_proyectil(pantalla)
            if not self.disparo_arriba:
                proyectil.trayecto_proyectil(velocidad)
            if self.disparo_arriba:
                proyectil.trayecto_proyectil_y(velocidad)

    def update_proyectiles(self,pantalla,velocidad):
        if self.vida >0:
            self.crear_proyectil_enemigo(velocidad)
            self.dibujar_listas_proyectiles(pantalla,self.lista_proyectiles_boss,velocidad)
    

    def verificar_colision_proyectil_boss_con_jugador(self,rectangulo_izquierda,rectangulo_derecha,rectangulo_bottom,rectangulo_top): ## revisar
        colisiono = False
        for proyectil in self.lista_proyectiles_boss:
            if proyectil.lados_proyectil["main"].colliderect(rectangulo_izquierda) or proyectil.lados_proyectil["main"].colliderect(rectangulo_derecha):
                self.lista_proyectiles_boss.remove(proyectil)
                colisiono = True
        return colisiono