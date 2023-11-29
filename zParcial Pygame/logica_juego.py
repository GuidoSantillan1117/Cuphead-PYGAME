import pygame
import sys
from render_images import *
from niveles import crear_nivel_1,crear_nivel_2,crear_nivel_3
from hitbox import hitbox_nivel_1,hitbox_nivel_2,hitbox_nivel_3
from functions import *
from animaciones import *
from modo_admin import *
from interfaz import *
from ranking import *
from musica_juego import *
import time

class LogicaJuego:
    def __init__(self):
        self.seleccionador_nivel = 0
        self.delay_opciones = 0.5
        pygame.init()
        pygame.mixer.init()
        self.timer_segundos = pygame.USEREVENT
        pygame.time.set_timer(self.timer_segundos, 100)

        self.timer_seconds = 60
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)

        self.width, self.height = 1280, 960
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Cuphead")

        self.font = pygame.font.Font(None, 70)
        self.font_nombre = pygame.font.Font(None, 120)
        self.font_score = pygame.font.Font(None, 24)
        self.font_ranking = pygame.font.Font(None, 30)


        self.fondo = pygame.image.load("zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/fondo_4k_2.jpg")
        self.fondo_dos = pygame.image.load("zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/fondo_4k.jpg")
        self.reescalar_fondo = pygame.transform.scale(self.fondo, (self.width, self.height))
        self.reescalar_fondo_dos = pygame.transform.scale(self.fondo_dos, (self.width, self.height))

        self.lista_fondos_movimiento = [
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_1.png",
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_2.png",
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_3.png",
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_4.png",
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_5.png",
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_6.png",
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_7.png",
            "zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/cielo_8.png"]

        self.lista_imagenes_plataformas = [
            "zParcial Pygame/imagenes_cuphead/plataformas/plataforma_uno.png",
            "zParcial Pygame/imagenes_cuphead/plataformas/prueba_plataforma.png",
            "zParcial Pygame/imagenes_cuphead/plataformas/tronco_uno.png",
            "zParcial Pygame/imagenes_cuphead/plataformas/plataforma_uno_girada.png"
        ]
        # self.lista_musica = [
        #     "testing duck copy 16/sonidos/nivel_1_musica.wav","testing duck copy 16/sonidos/nivel_2_musica.wav","testing duck copy 16/sonidos/nivel_3_musica.wav","testing duck copy 16/sonidos/musica_menu.wav"
        # ]
        self.animaciones_personaje = crear_animaciones_personaje()
        self.animaciones_personaje_nave = crear_animaciones_personaje_nave()
        self.animaciones_enemigos = crear_animaciones_enemigos()
        self.animaciones_enemigos_tiradores = crear_animaciones_enemigos_tiradores()
        self.animaciones_enemigos_planta_carnivora = crear_animaciones_enemigos_planta_carnivora()
        self.animaciones_boss = crear_animaciones_boss()
        self.lista_personajes = []
        self.lista_enemigos = []
        self.lista_enemigos_planta = []
        self.lista_boss = []
        self.lista_personajes_nave = []

        self.escribiendo = False
        self.nombre = ""

        self.contador_frames_fondo = 0
        self.mostrar_menu_nombre = True
        self.mostrar_menu = False
        self.entro_menu = False
        self.mostrar_seleccion_nivel = False
        self.mostrar_menu_muerte = False
        self.mostrar_menu_ranking = False
        self.mostrar_menu_win = False
        self.delay = False
        self.entro_nivel = False
        self.entro_nivel_1 = False
        self.entro_nivel_2 = False
        self.entro_nivel_3 = False
        self.entro_menu_win = False
        self.entro_seleccion_nivel = False
        self.entro_menu_muerte = False
        self.cancion_actual = None
        self.juego_en_pausa = False
        self.toco_esc = False
        self.bloqueo_jugar = False
        self.bloqueo_nivel_2 = True
        self.bloqueo_nivel_3 = True

        self.lista_opciones_menu_ingresar_nombre = escribir_nombre()
        self.lista_opciones_menu_principal = listar_opciones_menu_principal()
        self.lista_opciones_menu_ranking = listar_opciones_menu_ranking()
        self.lista_opciones_menu_seleccionar_nivel = listar_opciones_menu_seleccionar_nivel()
        self.lista_opciones_menu_pausa = listar_opciones_menu_pausa()
        self.lista_opciones_menu_muerte = listar_opciones_menu_muerte()
        self.lista_datos_ranking = obtener_valores_tabla()
        self.lista_opciones_menu_win = listar_opciones_menu_win()

        self.verificar_win_nivel_1 = False
        self.verificar_win_nivel_2 = False
        self.verificar_win_nivel_3 = False
        self.verificar_muerto_nivel_1 = False
        self.verificar_muerto_nivel_2 = False
        self.verificar_muerto_nivel_3 = False
        
        self.verificar_tiempo_nivel_1 = False
        self.verificar_tiempo_nivel_2 = False
        self.verificar_tiempo_nivel_3 = False
        self.score = 0
        self.score_win = 500
        self.puntos_extras = 0

        self.sonidos = Sonidos()




    def manejar_sonidos_musica_juego(self):
        self.sonidos.sonidos_entidades(self.lista_enemigos,self.lista_enemigos_planta, self.lista_boss,self.lista_personajes_nave,self.lista_personajes)
        self.manejar_musica()

    def manejar_musica(self):
        if self.entro_menu:
            self.sonidos.reproductor_canciones(self.sonidos.path_musica_menu_principal,0.05)
            self.entro_menu = False
        elif self.entro_nivel_1:
            self.sonidos.reproductor_canciones(self.sonidos.path_musica_nivel_1,0.05)
            self.entro_nivel_1 = False
        elif self.entro_nivel_2:
            self.sonidos.reproductor_canciones(self.sonidos.path_musica_nivel_2,0.05)
            self.entro_nivel_2 = False
        elif self.entro_nivel_3:
            self.sonidos.reproductor_canciones(self.sonidos.path_musica_nivel_3,0.05)
            self.entro_nivel_3 = False
        elif self.entro_menu_muerte:
            self.sonidos.reproductor_canciones(self.sonidos.path_musica_menu_muerte,0.05)
            self.entro_menu_muerte = False
        elif self.entro_seleccion_nivel:
            self.sonidos.reproductor_canciones(self.sonidos.path_musica_seleccion_nivel,0.05)
            self.entro_seleccion_nivel = False
        elif self.entro_menu_win:
            self.sonidos.reproductor_canciones(self.sonidos.path_musica_menu_muerte,0.05)
            self.entro_menu_win = False

    def cambiar_modo(self):
        cambiar_modo()


    def actualizar_interfaz(self):
        if self.mostrar_menu_nombre:
            menu_ingresar_nombre(self.screen)
            dibujar_nombre(self.screen, self.nombre, self.font_nombre, (340, 300))        

        if self.mostrar_menu:
            menu(self.screen)
            self.entro_nivel = False
        elif self.mostrar_seleccion_nivel:
            self.entro_nivel = False
            menu_seleccionar_nivel(self.screen)
            if not self.bloqueo_nivel_2 or not self.bloqueo_nivel_3:
                dibujar_score_menu_principal(self.screen, self.font_score, self.score, self.score_win,self.puntos_extras, self.width)
                dibujar_mensaje_alerta(self.screen, self.font_score, (640, 100))
        elif self.mostrar_menu_muerte:
                menu_muerte(self.screen)
        elif self.mostrar_menu_win:
            self.menu_win_partida()
            dibujar_score_menu_win(self.screen,self.font_nombre,self.score)

    def actualizar_niveles(self,datos):
        if datos is not None:
            if self.seleccionador_nivel == 1:
                self.crear_nivel_1(self.screen,datos["plataformas"],datos["enemigos"],datos["corazones"],datos["piso"],datos["personaje"])
            if self.seleccionador_nivel == 2:
                self.crear_nivel_2(datos["plataformas"],datos["plataformas_movil"],datos["enemigos"],datos["enemigos_planta"]
                                    ,datos["corazones"],datos["piso"],datos["personaje"])
            if self.seleccionador_nivel == 3:
                self.crear_nivel_3(datos["personaje_nave"],datos["boss_final"])

                if not self.juego_en_pausa:
                    self.contador_frames_fondo +=1
                if self.contador_frames_fondo >=8:
                    self.contador_frames_fondo = 0

    def actualizar_ranking(self):
        if self.mostrar_menu_ranking:
            lista_datos_ranking = obtener_valores_tabla()
            menu_ranking(self.screen)
            dibujar_valores_pantalla(self.screen,self.font,lista_datos_ranking)


    def manejar_contador_tiempo(self,):
        if self.entro_nivel:
            if self.timer_seconds >0 and not self.juego_en_pausa :
                if not self.verificar_win_nivel_1 or not self.verificar_win_nivel_2 or not self.verificar_win_nivel_3:
                    self.timer_seconds -=1
    def borrar_caracter(self):
        self.nombre = self.nombre[:-1]  

    def manejar_ingreso_nombre(self):
        print("Bienvenido ",self.nombre)
        self.escribiendo = False
        self.mostrar_menu_nombre = False
        self.mostrar_menu = True
        self.entro_menu = True

    def manejar_movimiento_personajes(self, keys, datos):      
        if datos is not None and not self.mostrar_menu and not self.mostrar_seleccion_nivel and not self.juego_en_pausa and not self.mostrar_menu_nombre and not self.mostrar_menu_muerte:
            if self.seleccionador_nivel == 1:
                manejar_input_personajes(keys, datos["personaje"])
            elif self.seleccionador_nivel == 2:
                manejar_input_personajes(keys, datos["personaje"])
            elif self.seleccionador_nivel == 3:
                manejar_input_personaje_nave(keys, datos["personaje_nave"])



    def manejar_disparo(self,datos):
        if datos is not None:
            if self.seleccionador_nivel == 1:
                manejar_input_disparo_personaje(datos["personaje"])
            if self.seleccionador_nivel ==2:
                manejar_input_disparo_personaje(datos["personaje"])
            if self.seleccionador_nivel ==3:
                manejar_input_disparo_personaje_nave(datos["personaje_nave"])

    def manejar_pausa(self):
        if not self.mostrar_menu and not self. mostrar_seleccion_nivel and not self.mostrar_menu_muerte and not self.mostrar_menu_nombre and not self.mostrar_menu_ranking and not self.mostrar_menu_win:
            self.toco_esc = True
            self.juego_en_pausa = not self.juego_en_pausa
            pygame.time.delay(100)
    def manejar_eventos_click(self,mouse_pos):
        if self.mostrar_menu_nombre:
            self.manejar_menu_nombre(mouse_pos)

        elif self.mostrar_menu:
            self.manejar_menu_principal(mouse_pos)

        elif self.mostrar_menu_ranking:
            self.manejar_menu_ranking(mouse_pos)

        if self.mostrar_menu_muerte:
            self.manejar_menu_muerte(mouse_pos)

        if self.juego_en_pausa:
            self.manejar_menu_pausa(mouse_pos)

        if self.mostrar_menu_win:
            self.manejar_menu_win(mouse_pos)

    def manejar_menu_win(self,mouse_pos):
        if verificar_click(self.lista_opciones_menu_win[0],mouse_pos):
            print("entre")
            self.mostrar_menu_win = False
            self.mostrar_menu = True
            self.entro_menu = True

    def manejar_menu_niveles(self, mouse_pos):
        if self.delay:
            mouse_pos = 0, 0
            self.delay = False
        datos = None

        if verificar_click(self.lista_opciones_menu_seleccionar_nivel[0], mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            self.score = 0
            self.entro_nivel = True
            self.entro_nivel_1 = True
            self.iniciar_valores_nivel()
            if not self.bloqueo_nivel_2:
                self.bloqueo_nivel_2 = True
            datos = self.generar_nivel_1()
            time.sleep(self.delay_opciones)
            self.seleccionador_nivel = 1
            self.mostrar_seleccion_nivel = False
            if datos is not None:
                return datos

        elif verificar_click(self.lista_opciones_menu_seleccionar_nivel[1], mouse_pos) and not self.bloqueo_nivel_2 and self.bloqueo_nivel_3:
            self.sonidos.manejar_sonido_menu(1)
            self.entro_nivel = True
            self.entro_nivel_2 = True
            self.iniciar_valores_nivel()
            time.sleep(self.delay_opciones)
            self.seleccionador_nivel = 2
            datos = self.generar_nivel_2()
            self.mostrar_seleccion_nivel = False
            if datos is not None:
                return datos

        elif verificar_click(self.lista_opciones_menu_seleccionar_nivel[2], mouse_pos) and not self.bloqueo_nivel_3:
            self.sonidos.manejar_sonido_menu(1)
            self.entro_nivel = True
            self.entro_nivel_3 = True
            self.iniciar_valores_nivel()
            time.sleep(self.delay_opciones)
            self.seleccionador_nivel = 3
            datos = self.generar_nivel_3()
            self.mostrar_seleccion_nivel = False
            if datos is not None:
                return datos

        elif verificar_click(self.lista_opciones_menu_seleccionar_nivel[3], mouse_pos):
            self.mostrar_seleccion_nivel = False
            self.mostrar_menu = True
            self.entro_menu = True

        

    def manejar_menu_ranking(self,mouse_pos):
        if verificar_click(self.lista_opciones_menu_ranking[0], mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            self.mostrar_menu = True
            self.entro_menu = True
            self.mostrar_menu_ranking = False

    def manejar_menu_muerte(self,mouse_pos):
        if verificar_click(self.lista_opciones_menu_muerte[0],mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            self.reiniciar_partida()

    def manejar_menu_pausa(self,mouse_pos):
        if verificar_click(self.lista_opciones_menu_pausa[0], mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            self.juego_en_pausa = False
            self.seleccionador_nivel = 4
        if verificar_click(self.lista_opciones_menu_pausa[1], mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            self.seleccionador_nivel = 0
            self.juego_en_pausa = False
            self.mostrar_menu = True
            self.entro_menu = True

    def manejar_menu_nombre(self,mouse_pos):
        if verificar_click(self.lista_opciones_menu_ingresar_nombre[0], mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            self.escribiendo = True
        else:
            self.escribiendo = False



    def manejar_menu_principal(self,mouse_pos):
        if verificar_click(self.lista_opciones_menu_principal[0], mouse_pos) and not self.bloqueo_jugar:
            self.sonidos.manejar_sonido_menu(1)
            self.mostrar_menu = False
            self.mostrar_seleccion_nivel = True
            self.entro_seleccion_nivel = True
            self.delay = True
        elif verificar_click(self.lista_opciones_menu_principal[1], mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            self.mostrar_menu = False
            self.mostrar_menu_ranking = True
        elif verificar_click(self.lista_opciones_menu_principal[2], mouse_pos):
            self.sonidos.manejar_sonido_menu(1)
            sys.exit()

    def menu_win_partida(self):
        if self.mostrar_menu_win:
            menu_win(self.screen)

    def mostrar_menu_pausa(self):
        if self.juego_en_pausa:
            menu_pausa(self.screen)
    def iniciar_valores_nivel(self):
        self.timer_seconds = 60
        self.mostrar_seleccion_nivel = False

    def verificar_muerto(self,personaje):
        if personaje.vida <= 0:
            return True

    def verificar_tiempo(self,tiempo):
        if tiempo <= 0:
            return True
            
    def generar_nivel_1(self):
        entidades_nivel_1 = crear_nivel_1(self.animaciones_personaje, self.animaciones_enemigos, self.animaciones_enemigos_tiradores,self.lista_imagenes_plataformas)
        if len(entidades_nivel_1) > 0:
            personaje_nivel_1 = entidades_nivel_1["personaje"]
            piso_nivel_1 = entidades_nivel_1["piso"]
            plataformas_nivel_1 = entidades_nivel_1["plataformas"]
            enemigos_nivel_1 = entidades_nivel_1["enemigos"]
            corazones_nivel_1 = entidades_nivel_1["corazones"]
            self.lista_personajes.append(personaje_nivel_1)
            self.lista_enemigos.append(enemigos_nivel_1)
        else:
            print("ERROR")

        return {
            "personaje": personaje_nivel_1,
            "piso": piso_nivel_1,
            "plataformas": plataformas_nivel_1,
            "enemigos": enemigos_nivel_1,
            "corazones": corazones_nivel_1
        }


    def generar_nivel_2(self):
        entidades_nivel_2 = crear_nivel_2(self.animaciones_personaje, self.animaciones_enemigos, self.animaciones_enemigos_tiradores, self.animaciones_enemigos_planta_carnivora, self.lista_imagenes_plataformas)
        if len(entidades_nivel_2) > 0:
            personaje_nivel_2 = entidades_nivel_2["personaje"]
            piso_nivel_2 = entidades_nivel_2["piso"]
            plataformas_nivel_2 = entidades_nivel_2["plataformas"]
            plataformas_movil_nivel_2 = entidades_nivel_2["plataformas_movil"]
            enemigos_nivel_2 = entidades_nivel_2["enemigos"]
            enemigos_planta_nivel_2 = entidades_nivel_2["enemigos_planta"]
            corazones_nivel_2 = entidades_nivel_2["corazones"]
            self.lista_personajes.append(personaje_nivel_2)
            self.lista_enemigos.append(enemigos_nivel_2)
            self.lista_enemigos_planta.append(enemigos_planta_nivel_2)
        else:
            print("ERROR")
        return {
            "personaje": personaje_nivel_2,
            "piso": piso_nivel_2,
            "plataformas": plataformas_nivel_2,
            "plataformas_movil" : plataformas_movil_nivel_2,
            "enemigos": enemigos_nivel_2,
            "enemigos_planta": enemigos_planta_nivel_2,
            "corazones": corazones_nivel_2
        }


    def generar_nivel_3(self):
        entidades_nivel_3 = crear_nivel_3(self.animaciones_personaje_nave, self.animaciones_boss)
        if len(entidades_nivel_3) > 0:
            personaje_nave = entidades_nivel_3["personaje_nave"]
            boss_final = entidades_nivel_3["boss"]
            self.lista_personajes_nave.append(personaje_nave)
            self.lista_boss.append(boss_final)
        else:
            print("ERROR")

        return {
            "personaje_nave": personaje_nave,
            "boss_final" : boss_final
        }


    def crear_nivel_1(self,pantalla,plataformas_nivel_1,enemigos_nivel_1,corazones_nivel_1,piso_nivel_1,personaje_nivel_1):
        self.bloqueo_nivel_3 = True
        creador_nivel(pantalla, plataformas_nivel_1, [], enemigos_nivel_1, [], corazones_nivel_1,self.reescalar_fondo, piso_nivel_1, personaje_nivel_1, 1130, 530)
        hitbox_nivel_1(pantalla, personaje_nivel_1, plataformas_nivel_1, enemigos_nivel_1)
        dibujar_string_pantalla(pantalla, self.font, self.timer_seconds, (self.width // 2, 40), "White")
        self.pausar_juego(enemigos_nivel_1,personaje_nivel_1,[])

        self.verificar_win_nivel_1 = verificar_win(personaje_nivel_1, 500, 650, enemigos_nivel_1)
        self.verificar_tiempo_nivel_1 = self.verificar_tiempo(self.timer_seconds)
        self.verificar_muerto_nivel_1 = verificar_muerto(personaje_nivel_1)
        if self.verificar_win_nivel_1:
            self.ganar_nivel_1()
            self.verificar_win_nivel_1 = False
        if self.verificar_muerto_nivel_1 or self.verificar_tiempo_nivel_1:
            self.morir_personaje()
            self.verificar_muerto_nivel_1 = False

    def crear_nivel_2(self,plataformas_nivel_2,plataformas_movil_nivel_2,enemigos_nivel_2,enemigos_planta_nivel_2,corazones_nivel_2,piso_nivel_2,personaje_nivel_2):
        creador_nivel(self.screen, plataformas_nivel_2, plataformas_movil_nivel_2, enemigos_nivel_2,enemigos_planta_nivel_2, corazones_nivel_2, self.reescalar_fondo_dos, piso_nivel_2, personaje_nivel_2, 1100, 50)
        hitbox_nivel_2(self.screen, personaje_nivel_2, plataformas_nivel_2, plataformas_movil_nivel_2,enemigos_nivel_2, enemigos_planta_nivel_2)
        dibujar_string_pantalla(self.screen, self.font, self.timer_seconds, (self.width // 2, 40), "Black")
        self.pausar_juego(enemigos_nivel_2,personaje_nivel_2,plataformas_movil_nivel_2)

        self.verificar_win_nivel_2 = verificar_win(personaje_nivel_2, 10, 60, enemigos_nivel_2)
        self.verificar_muerto_nivel_2 = verificar_muerto(personaje_nivel_2)
        self.verificar_tiempo_nivel_2 = self.verificar_tiempo(self.timer_seconds)
        if self.verificar_win_nivel_2:
            self.ganar_nivel_2()
            self.verificar_win_nivel_2 = False

        if self.verificar_muerto_nivel_2 or self.verificar_tiempo_nivel_2:
            self.morir_personaje()
            self.verificar_muerto_nivel_2 = False

    def crear_nivel_3(self,personaje_nave,boss_final):
        self.bloqueo_nivel_2 = True
        creador_nivel_final(self.screen,boss_final,self.lista_fondos_movimiento,personaje_nave,self.contador_frames_fondo)
        hitbox_nivel_3(self.screen, personaje_nave, boss_final)
        dibujar_string_pantalla(self.screen, self.font, self.timer_seconds, (self.width // 2, 40), "Black")
        self.pausar_juego_boss(personaje_nave,boss_final)
        self.verificar_win_nivel_3 = verificar_win_boss_final(boss_final)
        self.verificar_muerto_nivel_3 = verificar_muerto(personaje_nave)
        self.verificar_tiempo_nivel_3 = self.verificar_tiempo(self.timer_seconds)
        if self.verificar_win_nivel_3:
            self.ganar_nivel_3()
            self.verificar_win_nivel_3 = False

        if self.verificar_muerto_nivel_3 or self.verificar_tiempo_nivel_3:
            self.morir_personaje()
            self.verificar_muerto_nivel_3 = False

    def ganar_nivel_1(self):
        self.sumar_score(250)
        self.seleccionador_nivel = 0
        self.mostrar_seleccion_nivel = True
        self.entro_seleccion_nivel = True
        self.bloqueo_nivel_2 = False
    def ganar_nivel_2(self):
        self.sumar_score(500)
        self.seleccionador_nivel = 0
        self.mostrar_seleccion_nivel = True
        self.entro_seleccion_nivel = True
        self.bloqueo_nivel_3 = False
    def ganar_nivel_3(self):
        self.sumar_score(1000)
        agregar_valores_tabla(self.nombre,self.score)
        self.bloqueo_jugar = True
        self.seleccionador_nivel = 0
        self.mostrar_menu_win = True
        self.entro_menu_win = True



    def sumar_score(self,suma):
        self.score_win = suma
        self.score +=  self.score_win
        self.puntos_extras = calcular_puntos_extras(self.timer_seconds)
        self.score += self.puntos_extras


    def pausar_juego(self,enemigos,personaje,plataformas_movil):
        if self.juego_en_pausa:
            pausar_acciones(enemigos ,personaje,plataformas_movil)
        if not self.juego_en_pausa and self.toco_esc:
            despausar_acciones(enemigos,personaje,plataformas_movil)
            self.toco_esc = False

    def pausar_juego_boss(self,personaje_nave,boss_final):
        if self.juego_en_pausa:
            pausar_acciones_boss(personaje_nave,boss_final)
        if not self.juego_en_pausa and self.toco_esc:
            despausar_acciones_boss(personaje_nave,boss_final)
            self.toco_esc = False

    def morir_personaje(self):
        self.seleccionador_nivel = 0
        self.mostrar_menu_muerte = True
        self.entro_menu_muerte = True
    def reiniciar_partida(self):
        self.bloqueo_nivel_3 = True
        self.bloqueo_nivel_2 = True
        self.score = 0
        self.verificar_win_nivel_1 = False
        self.verificar_win_nivel_2 = False
        self.verificar_muerto_nivel_1 = False
        self.mostrar_menu_muerte = False
        self.mostrar_seleccion_nivel = True
        self.entro_seleccion_nivel = True