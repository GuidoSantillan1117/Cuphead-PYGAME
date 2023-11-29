import pygame 

def girar_personaje(lista_animacion,flip_x,flip_y):
    lista_girada = []
    for frame in lista_animacion:
        lista_girada.append(pygame.transform.flip(frame,flip_x,flip_y))
    return lista_girada

def reescalar_imagen(lista_animacion,tamaño):
    for i in range (len(lista_animacion)):
        lista_animacion[i] = pygame.transform.scale(lista_animacion[i],(tamaño))

def obtener_rectangulos(principal:pygame.Rect,px:int):

    diccionario_rectangulos = {}
    diccionario_rectangulos["main"] = principal
    diccionario_rectangulos["top"] = pygame.Rect(principal.left, principal.top,principal.width, px)
    diccionario_rectangulos["right"] = pygame.Rect(principal.right-(px),principal.top,px,principal.height)
    diccionario_rectangulos["left"] = pygame.Rect(principal.left,principal.top,px,principal.height)
    diccionario_rectangulos["bottom"] = pygame.Rect(principal.left,principal.bottom -(px),principal.width,px)
    return diccionario_rectangulos

def obtener_rectangulos_plataforma(principal:pygame.Rect):
    diccionario_rectangulos = {}
    diccionario_rectangulos["main"] = principal
    diccionario_rectangulos["top"] = pygame.Rect(principal.left, principal.top,principal.width, 30)
    diccionario_rectangulos["right"] = pygame.Rect(principal.right-(10),principal.top,10,principal.height)
    diccionario_rectangulos["left"] = pygame.Rect(principal.left,principal.top,10,principal.height)
    diccionario_rectangulos["bottom"] = pygame.Rect(principal.left,principal.bottom -(30),principal.width,30)
    return diccionario_rectangulos


personaje_derecha = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0001.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0002.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0003.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0004.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0005.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0006.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0007.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0008.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0012.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0013.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_run_0014.png")]

personaje_quieto_derecha = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_idle_0001.png"),
                            pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_idle_0002.png"),
                            pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_idle_0003.png"),
                            pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_idle_0004.png"),
                            pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_idle_0005.png")]

personaje_quieto_derecha_dañado = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/personaje_dañado/dañado_quieto.png")]

personaje_saltando_derecha =    [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0001.png"),
                                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0002.png"),
                                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0003.png"),
                                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0004.png"),
                                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0005.png"),
                                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0006.png"),
                                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0007.png"),
                                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_jump_0008.png")]
personaje_saltando_derecha_dañado = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/personaje_dañado/dañado_saltando.png")]

personaje_agachado_derecha = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_duck_0001.png"),
                            pygame.image.load("zParcial Pygame/imagenes_cuphead\personaje_cuphead/cuphead_duck_0002.png"),
                            pygame.image.load("zParcial Pygame/imagenes_cuphead\personaje_cuphead/cuphead_duck_0004.png"),
                            pygame.image.load("zParcial Pygame/imagenes_cuphead\personaje_cuphead/cuphead_duck_0005.png")]

personaje_agachado_derecha_dañado = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/personaje_dañado/dañado_agachado.png")]

personaje_dañado_derecha = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/personaje_dañado/dañado_derecha.png")]


nave_derecha = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_nave/cuphead_plane_idle_straight_0001.png"),
                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_nave/cuphead_plane_idle_straight_0002.png"),
                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_nave/cuphead_plane_idle_straight_0003.png"),
                pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_nave/cuphead_plane_idle_straight_0004.png")]



boss_izquierda = [
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0001.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0002.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0003.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0004.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0005.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0006.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0007.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0008.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0009.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0010.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0011.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0012.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0013.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0014.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0015.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0016.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0017.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0018.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0019.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0020.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/blimp_idle_0021.png")]

boss_izquierda_dañado = [
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_1.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_2.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_3.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_4.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_5.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_6.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_7.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_8.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_9.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_10.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_11.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_12.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_13.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_14.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_15.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_15.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_16.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_17.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_18.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_19.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_20.png"),
    pygame.image.load("zParcial Pygame/imagenes_cuphead/boss_final/boss_final_dañado/boss_dañado_21.png")
]


enemigo_uno_derecha = [
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0001.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0002.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0003.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0004.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0005.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0006.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0007.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0008.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/blob_run_0009.png")]

enemigo_uno_derecha_dañado = [pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_azul/enemigo_azul_dañado.png")]
enemigo_dos_derecha_dañado = [pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_tirador/enemigo_planta_dañado.png")]

enemigo_dos_derecha = [
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_tirador/lobber_idle_0012.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_tirador/lobber_idle_0013.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_tirador/lobber_idle_0014.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_tirador/lobber_idle_0015.png"),
                    pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_tirador/lobber_idle_0016.png")]

enemigo_tres_quieto = [pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_planta/chomper_attack_0001.png")]

enemigo_tres_ataque = [
                        pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_planta/chomper_attack_0009.png"),
                        pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_planta/chomper_attack_0010.png"),
                        pygame.image.load("zParcial Pygame/imagenes_cuphead/enemigo_planta/chomper_attack_0011.png")]

lista_plataformas = [pygame.image.load("zParcial Pygame/imagenes_cuphead/plataformas/prueba_plataforma.png")]




personaje_disparando_derecha = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_shoot_straight_0001.png")]
personaje_disparando_agachado_derecha = [pygame.image.load("zParcial Pygame/imagenes_cuphead/personaje_cuphead/cuphead_duck_shoot_0001.png")]




personaje_izquierda = girar_personaje(personaje_derecha,True,False)
personaje_quieto_izquierda = girar_personaje(personaje_quieto_derecha,True,False)
personaje_saltando_izquierda = girar_personaje(personaje_saltando_derecha,True,False)
personaje_disparando_izquierda = girar_personaje(personaje_disparando_derecha,True,False)
personaje_agachado_izquierda = girar_personaje(personaje_agachado_derecha,True,False)
personaje_disparando_agachado_izquierda = girar_personaje(personaje_disparando_agachado_derecha,True,False)

personaje_dañado_izquierda = girar_personaje(personaje_dañado_derecha,True,False)
personaje_quieto_izquierda_dañado = girar_personaje(personaje_quieto_derecha_dañado,True,False)
personaje_saltando_izquierda_dañado = girar_personaje(personaje_saltando_derecha_dañado,True,False)
personaje_agachado_izquierda_dañado = girar_personaje(personaje_agachado_derecha_dañado,True,False)

nave_izquierda = girar_personaje(nave_derecha,True,False)

enemigo_uno_izquierda = girar_personaje(enemigo_uno_derecha,True,False)
enemigo_uno_izquierda_dañado = girar_personaje(enemigo_uno_derecha_dañado,True,False)

enemigo_dos_izquierda = girar_personaje(enemigo_dos_derecha,True,False)
enemigo_dos_izquierda_dañado = girar_personaje(enemigo_dos_derecha_dañado,True,False)

boss_derecha = girar_personaje(boss_izquierda,True,False)
boss_derecha_dañado = girar_personaje(boss_izquierda_dañado,True,False)
