from render_images import *
def crear_animaciones_personaje():
    diccionario_animaciones = {}

    diccionario_animaciones["derecha"] = personaje_derecha
    diccionario_animaciones["quieto_derecha"] = personaje_quieto_derecha
    diccionario_animaciones["izquierda"] = personaje_izquierda
    diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
    diccionario_animaciones["salta_derecha"] = personaje_saltando_derecha
    diccionario_animaciones["salta_izquierda"] = personaje_saltando_izquierda
    diccionario_animaciones["disparo_derecha"] = personaje_disparando_derecha
    diccionario_animaciones["disparo_izquierda"] = personaje_disparando_izquierda
    diccionario_animaciones["agachado_derecha"] = personaje_agachado_derecha
    diccionario_animaciones["agachado_izquierda"] = personaje_agachado_izquierda
    diccionario_animaciones["disparo_agachado_derecha"] = personaje_disparando_agachado_derecha
    diccionario_animaciones["disparo_agachado_izquierda"] = personaje_disparando_agachado_izquierda
    diccionario_animaciones["recibe_daño_derecha"] = personaje_dañado_derecha
    diccionario_animaciones["recibe_daño_izquierda"] = personaje_dañado_izquierda
    diccionario_animaciones["recibe_daño_quieto_derecha"] = personaje_quieto_derecha_dañado
    diccionario_animaciones["recibe_daño_quieto_izquierda"] = personaje_quieto_izquierda_dañado
    diccionario_animaciones["recibe_daño_salta_derecha"] = personaje_saltando_derecha_dañado
    diccionario_animaciones["recibe_daño_salta_izquierda"] = personaje_saltando_izquierda_dañado
    diccionario_animaciones["recibe_daño_agachado_derecha"] =  personaje_agachado_derecha_dañado
    diccionario_animaciones["recibe_daño_agachado_izquierda"] = personaje_agachado_izquierda_dañado

    return diccionario_animaciones

def crear_animaciones_personaje_nave():
    diccionario_animaciones_nave = {}

    diccionario_animaciones_nave["derecha"] = nave_derecha
    diccionario_animaciones_nave["izquierda"] = nave_izquierda

    return diccionario_animaciones_nave 

def crear_animaciones_enemigos():
    diccionario_animaciones_enemigo = {}

    diccionario_animaciones_enemigo["derecha"] = enemigo_uno_derecha
    diccionario_animaciones_enemigo["izquierda"] = enemigo_uno_izquierda
    diccionario_animaciones_enemigo["derecha_dañado"] = enemigo_uno_derecha_dañado
    diccionario_animaciones_enemigo["izquierda_dañado"] = enemigo_uno_izquierda_dañado

    return diccionario_animaciones_enemigo

def crear_animaciones_enemigos_tiradores():
    diccionario_animaciones_enemigos_tiradores = {}

    diccionario_animaciones_enemigos_tiradores["derecha"] = enemigo_dos_derecha
    diccionario_animaciones_enemigos_tiradores["izquierda"] = enemigo_dos_izquierda
    diccionario_animaciones_enemigos_tiradores["derecha_dañado"] = enemigo_dos_derecha_dañado
    diccionario_animaciones_enemigos_tiradores["izquierda_dañado"] = enemigo_dos_izquierda_dañado

    return diccionario_animaciones_enemigos_tiradores

def crear_animaciones_enemigos_planta_carnivora():
    diccionario_animaciones_enemigos_planta_carnivora = {}
    diccionario_animaciones_enemigos_planta_carnivora ["quieto"] = enemigo_tres_quieto
    diccionario_animaciones_enemigos_planta_carnivora ["ataca"] = enemigo_tres_ataque

    return diccionario_animaciones_enemigos_planta_carnivora

def crear_animaciones_boss():
    diccionario_animaciones_boss = {}
    diccionario_animaciones_boss ["izquierda"] = boss_izquierda
    diccionario_animaciones_boss ["derecha"] = boss_derecha
    diccionario_animaciones_boss ["izquierda_dañado"] = boss_izquierda_dañado 
    diccionario_animaciones_boss ["derecha_dañado"] = boss_derecha_dañado 
    return diccionario_animaciones_boss

