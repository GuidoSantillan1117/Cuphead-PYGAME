import pygame

def reescalar_imagen(imagen,tamaño):
    imagen_menu = pygame.image.load(imagen)
    imagen_menu_reescalada = pygame.transform.scale(imagen_menu,tamaño)
    return imagen_menu_reescalada

def blitear_menu(pantalla,imagen,tamaño,posicion):
    imagen = reescalar_imagen(imagen,tamaño) 
    pantalla.blit(imagen,posicion)


def crear_rectangulo_opciones(posicion_x,posicion_y,tamaño):
    rectangulo = pygame.Rect(posicion_x,posicion_y,tamaño[0],tamaño[1])
    return rectangulo

def hitbox_opciones(pantalla,rectangulo):
    pygame.draw.rect(pantalla,"Red",rectangulo,2)


def verificar_click(rect,mouse_pos):
    return rect.collidepoint(mouse_pos)

def menu(pantalla):
    blitear_menu(pantalla,"zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/menu.png",(1280,960),(0,0))
    
def menu_seleccionar_nivel(pantalla):
    blitear_menu(pantalla,"zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/menu_seleccionar_nivel.png",(1280,960),(0,0))

def menu_pausa(pantalla):
    blitear_menu(pantalla,"zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/menu_pausa.png",(600,600),(340,135))

def menu_muerte(pantalla):
    blitear_menu(pantalla,"zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/menu_muerto.png",(1280,960),(0,0))

def menu_ingresar_nombre(pantalla):
    blitear_menu(pantalla,"zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/menu_nombre.png",(1280,960),(0,0))

def menu_ranking(pantalla):
    blitear_menu(pantalla,"zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/menu_ranking.png",(1280,960),(0,0))

def menu_win(pantalla):
    blitear_menu(pantalla,"zParcial Pygame/imagenes_cuphead/Menu_interfaz_fondos/menu_win.png",(1280,960),(0,0))

def escribir_nombre():
    lista_opciones = []
    escribir_nombre = crear_rectangulo_opciones(256,275,(766,135))
    lista_opciones.append(escribir_nombre)
    return lista_opciones
def listar_opciones_menu_principal():
    lista_opciones = []
    opcion_jugar = crear_rectangulo_opciones(790,330,(260,90))
    opcion_ranking = crear_rectangulo_opciones(782,485,(380,80))
    opcion_salir = crear_rectangulo_opciones(785,655,(235,80))

    lista_opciones.append(opcion_jugar)
    lista_opciones.append(opcion_ranking)
    lista_opciones.append(opcion_salir)

    return lista_opciones

def listar_opciones_menu_seleccionar_nivel():
    lista_opciones = []
    opcion_nivel_1 = crear_rectangulo_opciones(48,289,(367,354))
    opcion_nivel_2 = crear_rectangulo_opciones(455,289,(368,354))
    opcion_nivel_3 = crear_rectangulo_opciones(864,289,(368,354))
    opcion_salir = crear_rectangulo_opciones(550,840,(180,56))

    lista_opciones.append(opcion_nivel_1)
    lista_opciones.append(opcion_nivel_2)
    lista_opciones.append(opcion_nivel_3)
    lista_opciones.append(opcion_salir)

    return lista_opciones
def listar_opciones_menu_ranking():
    lista_opciones = []
    opcion_salir = crear_rectangulo_opciones(560,845,(158,60))
    lista_opciones.append(opcion_salir)
    return lista_opciones
def listar_opciones_menu_pausa():
    lista_opciones = []
    opcion_reiniciar = crear_rectangulo_opciones(485,323,(305,57))
    opcion_salir = crear_rectangulo_opciones(558,460,(165,53))

    lista_opciones.append(opcion_reiniciar)
    lista_opciones.append(opcion_salir)

    return lista_opciones

def listar_opciones_menu_muerte():
    lista_opciones = []
    opcion_menu = crear_rectangulo_opciones(425,498,(435,50))

    lista_opciones.append(opcion_menu)

    return lista_opciones
def listar_opciones_menu_win():
    lista_opciones = []
    opcion_salir = crear_rectangulo_opciones(425,780,(435,50))
    lista_opciones.append(opcion_salir)
    return lista_opciones


    


