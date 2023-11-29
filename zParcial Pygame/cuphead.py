from logica_juego import LogicaJuego

import pygame
import sys

class Juego:
    def __init__(self, logica_juego):
        self.RELOJ = pygame.time.Clock()
        self.FPS = 30
        self.datos = None
        self.logica_juego = logica_juego() 
        pygame.init()
        pygame.mixer.init()

    def ejecutar(self):
        while True:
            self.logica_juego.actualizar_interfaz() 
            keys = pygame.key.get_pressed()
            self.logica_juego.manejar_movimiento_personajes(keys, self.datos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == self.logica_juego.timer_event:
                    self.logica_juego.manejar_contador_tiempo()
                elif event.type == pygame.KEYDOWN and self.logica_juego.escribiendo:
                    if event.key == pygame.K_RETURN:
                        self.logica_juego.manejar_ingreso_nombre()
                    elif event.key == pygame.K_BACKSPACE:
                        self.logica_juego.borrar_caracter() 
                    else:
                        self.logica_juego.nombre += event.unicode
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                    self.logica_juego.cambiar_modo()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.logica_juego.manejar_disparo(self.datos)
                    elif event.key == pygame.K_ESCAPE:
                        self.logica_juego.manejar_pausa()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    print("Posición del mouse:", mouse_pos)
                    self.logica_juego.manejar_eventos_click(mouse_pos)
                    if self.logica_juego.mostrar_seleccion_nivel:
                        self.datos = self.logica_juego.manejar_menu_niveles(mouse_pos)   

            self.logica_juego.manejar_sonidos_musica_juego()
            self.logica_juego.actualizar_interfaz()
            self.logica_juego.actualizar_niveles(self.datos)
            self.logica_juego.mostrar_menu_pausa()
            self.logica_juego.actualizar_ranking()
            
            pygame.display.flip()
            self.RELOJ.tick(self.FPS)

cuphead = Juego(LogicaJuego)
cuphead.ejecutar()

