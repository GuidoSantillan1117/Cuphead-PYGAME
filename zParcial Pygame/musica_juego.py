import pygame
class Sonidos():
    def __init__(self) -> None:
        self.path_sonidos_personaje = "zParcial Pygame/sonidos/player_spreadshot_fire_loop.wav"    
        self.path_sonidos_personaje_nave = "zParcial Pygame/sonidos/ataque_nave.wav"
        self.path_sonidos_enemigos = "zParcial Pygame/sonidos/Flower Cuphead Sound Effects HD.mp3"
        self.path_sonidos_enemigos_planta = "zParcial Pygame/sonidos/Eating sound effect LUCAS ARPON TV (mp3cut.net).wav"
        self.path_sonidos_boss_1 = "zParcial Pygame/sonidos/grito_ataque_normal.wav"
        self.path_sonidos_boss_2  = "zParcial Pygame/sonidos/grito_ataque_arriba.wav"

        self.path_musica_menu_principal = "zParcial Pygame/sonidos/musica_menu.wav"
        self.path_musica_seleccion_nivel = "zParcial Pygame/sonidos/Cuphead OST - Elder Kettle [Music].wav"
        self.path_musica_nivel_1 = "zParcial Pygame/sonidos/nivel_1_musica.wav"
        self.path_musica_nivel_2 = "zParcial Pygame/sonidos/nivel_2_musica.wav"
        self.path_musica_nivel_3 = "zParcial Pygame/sonidos/nivel_3_musica.wav"
        self.path_musica_boss = "zParcial Pygame/sonidos/boss_sonido_move.wav"
        self.path_musica_personaje_nave = "zParcial Pygame/sonidos/personaje_nave_sonido_avioneta.wav"
        self.path_musica_menu_muerte = "zParcial Pygame/sonidos/menu_muerte_musica.wav"
        self.path_musica_menu_win = "zParcial Pygame/sonidos/musica_win.wav"
        pygame.mixer.init()

    def cargar_musica(self, ruta):
        pygame.mixer.music.load(ruta)


    def reproducir_musica(self):
        pygame.mixer.music.play(loops=-1)
    

    def ajustar_volumen(self, volumen):
        pygame.mixer.music.set_volume(volumen)
    def detener_musica(self):
        pygame.mixer.music.stop()


    def cargar_sonido(self, ruta):
        self.sonido = pygame.mixer.Sound(ruta)

    def reproducir_sonido(self):
        self.sonido.set_volume(0.05)
        self.sonido.play()


    def detener_sonido(self):
        self.sonido.stop()

    def manejar_sonido_menu(self,sonido):
        if sonido == 1:
            self.cargar_sonido("zParcial Pygame/sonidos/Menu_Move.wav")
            self.sonido.play()

    def reproductor_canciones(self,path,volumen):
            self.cargar_musica(path)
            self.ajustar_volumen(volumen)
            self.reproducir_musica()


    def sonidos_entidades(self,lista_enemigos,lista_enemigos_planta,lista_boss,lista_personajes_nave,lista_personajes):
        self.sonidos_enemigos(lista_enemigos)
        self.sonidos_enemigos_planta(lista_enemigos_planta)
        self.sonidos_boss(lista_boss)
        self.sonidos_personaje_nave(lista_personajes_nave)
        self.sonidos_personaje(lista_personajes)
        

    def sonidos_personaje(self,lista_personajes):
        for personaje in lista_personajes:
            if personaje.que_hace == "dispara" and personaje.vida >0:
                self.cargar_sonido(self.path_sonidos_personaje)
                self.reproducir_sonido()

    def sonidos_enemigos(self,lista_enemigos):
        for nivel in lista_enemigos:
            for enemigo in nivel:
                if enemigo.vida_enemigo >0 and enemigo.enemigo_disparo:
                    self.cargar_sonido(self.path_sonidos_enemigos)
                    self.reproducir_sonido()
                    enemigo.enemigo_disparo = False
                    
    def sonidos_enemigos_planta(self,lista_enemigos_planta):
        for nivel in lista_enemigos_planta:
            for planta in nivel:
                if planta.ataque:
                    self.cargar_sonido(self.path_sonidos_enemigos_planta)
                    self.reproducir_sonido()
                    planta.ataque = False

    def sonidos_boss(self,lista_boss):
        for boss in lista_boss:
            if boss.vida>0:
                if boss.ataque_normal:
                    self.cargar_sonido(self.path_sonidos_boss_1)
                    self.reproducir_sonido()
                    boss.ataque_normal = False
                if boss.ataque_arriba:
                    self.cargar_sonido(self.path_sonidos_boss_2)
                    self.reproducir_sonido()
                    boss.ataque_arriba = False


    def sonidos_personaje_nave(self,lista_personajes_nave):
        for personaje_nave in lista_personajes_nave:
            if personaje_nave.vida >0:
                if personaje_nave.que_hace == "dispara":
                    self.cargar_sonido(self.path_sonidos_personaje_nave)
                    self.reproducir_sonido()
