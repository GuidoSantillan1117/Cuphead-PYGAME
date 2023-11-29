from personaje_principal import Personaje
from personaje_principal_nave import PersonajeNave
from planta_carnivora import PlantaCarnivora
from plataformas_movil import PlataformaMovil
from plataformas import Plataforma
from enemigos import Enemigos
from boss import BossFinal
from corazones import Corazones

def crear_nivel_1(diccionario_animaciones,diccionario_animaciones_enemigo,diccionario_animaciones_enemigos_tiradores,lista_imagenes_plataformas):
    diccionario_nivel_1 = {}
    mi_personaje_nivel_uno = Personaje(diccionario_animaciones,100,500)
    piso_uno = Plataforma(lista_imagenes_plataformas[0],-200,mi_personaje_nivel_uno.lados["bottom"].bottom-10,(1780,80)) 

    lista_plataformas_nivel_uno = []
    lista_enemigos_nivel_uno = []
    lista_corazones_nivel_uno = []

    enemigo_azul_01 = Enemigos(550,450,diccionario_animaciones_enemigo,False,550,1050,1,0,10)
    enemigo_azul_02 = Enemigos(530,150,diccionario_animaciones_enemigo,False,530,1280,1,0,10)
    enemigo_tirador_01 = Enemigos(0,175,diccionario_animaciones_enemigos_tiradores,True,0,0,1,30,5)
    enemigo_tirador_02 = Enemigos(1100,580,diccionario_animaciones_enemigos_tiradores,True,0,0,-1,50,5)

    plataforma_01_nivel_uno = Plataforma(lista_imagenes_plataformas[0],550,enemigo_azul_01.lados_enemigo["bottom"].bottom-13,(500,40))
    plataforma_02_nivel_uno = Plataforma(lista_imagenes_plataformas[0],-100,400,(450,40))
    plataforma_03_nivel_uno = Plataforma(lista_imagenes_plataformas[0],550,enemigo_azul_02.lados_enemigo["bottom"].bottom-13,(750,40)) #TENIA
    plataforma_04_nivel_uno = Plataforma(lista_imagenes_plataformas[0],-100,enemigo_tirador_01.lados_enemigo["bottom"].bottom-10,(250,40))

    corazon_01_nivel_uno = Corazones(770,505)

    lista_enemigos_nivel_uno.append(enemigo_azul_01)
    lista_enemigos_nivel_uno.append(enemigo_azul_02)
    lista_enemigos_nivel_uno.append(enemigo_tirador_01)
    lista_enemigos_nivel_uno.append(enemigo_tirador_02)

    lista_plataformas_nivel_uno.append(plataforma_01_nivel_uno)
    lista_plataformas_nivel_uno.append(plataforma_02_nivel_uno)
    lista_plataformas_nivel_uno.append(plataforma_03_nivel_uno)
    lista_plataformas_nivel_uno.append(plataforma_04_nivel_uno)

    lista_corazones_nivel_uno.append(corazon_01_nivel_uno)
    
    diccionario_nivel_1 ["personaje"] = mi_personaje_nivel_uno
    diccionario_nivel_1 ["piso"] = piso_uno
    diccionario_nivel_1 ["plataformas"] = lista_plataformas_nivel_uno
    diccionario_nivel_1 ["enemigos"] = lista_enemigos_nivel_uno
    diccionario_nivel_1["corazones"] = lista_corazones_nivel_uno

    return diccionario_nivel_1

def crear_nivel_2(diccionario_animaciones,diccionario_animaciones_enemigo,diccionario_animaciones_enemigos_tiradores,diccionario_animaciones_enemigos_planta_carnivora,lista_imagenes_plataformas):
    diccionario_nivel_2 = {}
    mi_personaje_nivel_dos = Personaje(diccionario_animaciones,100,750)
    piso_dos = Plataforma(lista_imagenes_plataformas[1],-200,mi_personaje_nivel_dos.lados["bottom"].bottom-10,(1780,100))

    lista_plataformas_nivel_dos = []
    lista_enemigos_nivel_dos = []
    lista_plantas_nivel_dos = []
    lista_plataformas_movil_nivel_dos = []
    lista_corazones_nivel_dos = []

    plataforma_01_nivel_dos = Plataforma(lista_imagenes_plataformas[0],350,760,(150,40))
    plataforma_02_nivel_dos = Plataforma(lista_imagenes_plataformas[0],700,760,(150,40))
    plataforma_03_nivel_dos = Plataforma(lista_imagenes_plataformas[0],400,160,(300,40))
    plataforma_04_nivel_dos = Plataforma(lista_imagenes_plataformas[2],-20,280,(100,240))
    plataforma_06_nivel_dos = Plataforma(lista_imagenes_plataformas[0],-100,510,(950,80))
    plataforma_07_nivel_dos = Plataforma(lista_imagenes_plataformas[0],250,370,(600,40))
    plataforma_08_nivel_dos = Plataforma(lista_imagenes_plataformas[0],-20,260,(100,20)) 

    plataforma_win_nivel_dos = Plataforma(lista_imagenes_plataformas[0],1050,150,(280,40))

    tronco_01_nivel_dos = Plataforma(lista_imagenes_plataformas[2],1000,piso_dos.lados_plataforma["top"].top-70,(150,80),True)
    plataforma_movil_01_nivel_dos = PlataformaMovil(lista_imagenes_plataformas[1],600,260,(200,50),280,1000)

    enemigo_azul_01_nivel_dos = Enemigos(400,60,diccionario_animaciones_enemigo,False,400,700,1,0,10)

    enemigo_tirador_01_nivel_dos = Enemigos(0,200,diccionario_animaciones_enemigos_tiradores,True,0,0,1,30,5)
    enemigo_tirador_02_nivel_dos = Enemigos(740,450,diccionario_animaciones_enemigos_tiradores,True,0,0,-1,50,5)
    enemigo_planta_01 = PlantaCarnivora(235,830,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_03 = PlantaCarnivora(500,830,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_04 = PlantaCarnivora(enemigo_planta_03.lados_planta["right"].right+5,830,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_05 = PlantaCarnivora(tronco_01_nivel_dos.lados_plataforma["left"].left-130,830,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_07 = PlantaCarnivora(tronco_01_nivel_dos.lados_plataforma["right"].right+10,830,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_08 = PlantaCarnivora(270,310,diccionario_animaciones_enemigos_planta_carnivora,(110,60))
    enemigo_planta_09 = PlantaCarnivora(enemigo_planta_08.lados_planta["right"].right+ 10,310,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_10 = PlantaCarnivora(enemigo_planta_09.lados_planta["right"].right+ 10,310,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_11 = PlantaCarnivora(enemigo_planta_10.lados_planta["right"].right+ 10,310,diccionario_animaciones_enemigos_planta_carnivora,(100,60))
    enemigo_planta_12 = PlantaCarnivora(enemigo_planta_11.lados_planta["right"].right+ 10,310,diccionario_animaciones_enemigos_planta_carnivora,(100,60))

    corazon_01_nivel_dos = Corazones(520,120)
    corazon_02_nivel_dos = Corazones(100,470)

    lista_plataformas_nivel_dos.append(plataforma_01_nivel_dos)
    lista_plataformas_nivel_dos.append(plataforma_02_nivel_dos)
    lista_plataformas_nivel_dos.append(plataforma_03_nivel_dos)
    lista_plataformas_nivel_dos.append(plataforma_04_nivel_dos)
    lista_plataformas_nivel_dos.append(plataforma_06_nivel_dos)
    lista_plataformas_nivel_dos.append(plataforma_07_nivel_dos)
    lista_plataformas_nivel_dos.append(plataforma_08_nivel_dos)
    lista_plataformas_nivel_dos.append(plataforma_win_nivel_dos)
    lista_plataformas_nivel_dos.append(tronco_01_nivel_dos)

    lista_plataformas_movil_nivel_dos.append(plataforma_movil_01_nivel_dos)

    lista_enemigos_nivel_dos.append(enemigo_azul_01_nivel_dos)
    lista_enemigos_nivel_dos.append(enemigo_tirador_01_nivel_dos)
    lista_enemigos_nivel_dos.append(enemigo_tirador_02_nivel_dos)

    lista_plantas_nivel_dos.append(enemigo_planta_01)
    lista_plantas_nivel_dos.append(enemigo_planta_03)
    lista_plantas_nivel_dos.append(enemigo_planta_04)
    lista_plantas_nivel_dos.append(enemigo_planta_05)
    lista_plantas_nivel_dos.append(enemigo_planta_07)
    lista_plantas_nivel_dos.append(enemigo_planta_08)
    lista_plantas_nivel_dos.append(enemigo_planta_09)
    lista_plantas_nivel_dos.append(enemigo_planta_10)
    lista_plantas_nivel_dos.append(enemigo_planta_11)
    lista_plantas_nivel_dos.append(enemigo_planta_12)

    lista_corazones_nivel_dos.append(corazon_01_nivel_dos)
    lista_corazones_nivel_dos.append(corazon_02_nivel_dos)

    diccionario_nivel_2 ["personaje"] = mi_personaje_nivel_dos
    diccionario_nivel_2 ["piso"] = piso_dos
    diccionario_nivel_2 ["plataformas"] = lista_plataformas_nivel_dos
    diccionario_nivel_2 ["plataformas_movil"] = lista_plataformas_movil_nivel_dos
    diccionario_nivel_2 ["enemigos"] = lista_enemigos_nivel_dos
    diccionario_nivel_2 ["enemigos_planta"] = lista_plantas_nivel_dos
    diccionario_nivel_2["corazones"] = lista_corazones_nivel_dos

    return diccionario_nivel_2

def crear_nivel_3(diccionario_animaciones_personaje_nave,diccionario_animaciones_boss):
    diccionario_nivel_3 = {}
    personaje_nave = PersonajeNave(200,300,diccionario_animaciones_personaje_nave)
    boss_final = BossFinal(diccionario_animaciones_boss)

    diccionario_nivel_3 ["personaje_nave"] = personaje_nave
    diccionario_nivel_3 ["boss"] = boss_final

    return diccionario_nivel_3