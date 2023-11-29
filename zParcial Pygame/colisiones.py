import pygame

def manejar_colisiones(mi_personaje,piso,lista_plataformas,lista_plataformas_movil):
    verificar_piso = verificar_colision(mi_personaje.lados["bottom"], piso.lados_plataforma["top"])
    if verificar_piso:
        mi_personaje.esta_saltando = False
        mi_personaje.potencia_salto = -17
        ajustar_posicion_jugador(mi_personaje,mi_personaje.lados["bottom"].y,piso.lados_plataforma["top"].y)

    for plataforma in lista_plataformas:
        colisiono_bottom = verificar_colision(mi_personaje.lados["bottom"], plataforma.lados_plataforma["top"])
        colisiono_top = verificar_colision(mi_personaje.lados["top"], plataforma.lados_plataforma["bottom"])
        colisiono_right = verificar_colision(mi_personaje.lados["right"], plataforma.lados_plataforma["left"])
        colisiono_left = verificar_colision(mi_personaje.lados["left"], plataforma.lados_plataforma["right"])
        colisiono_top_agachado = verificar_colision(mi_personaje.lados_agachado["top"],plataforma.lados_plataforma["bottom"])
    
        if colisiono_bottom:
            if mi_personaje.esta_saltando:
                mi_personaje.esta_saltando = False
                mi_personaje.potencia_salto = -17
                ajustar_posicion_jugador(mi_personaje,mi_personaje.lados["bottom"].y,plataforma.lados_plataforma["top"].y)
                if plataforma.es_tronco:
                    mi_personaje.potencia_salto = -40

        if colisiono_right and colisiono_bottom:
            mi_personaje.esta_saltando = True
            mi_personaje.desplazamiento_y = 10

        if colisiono_left and colisiono_bottom:
            mi_personaje.esta_saltando = True
            mi_personaje.desplazamiento_y = 10

        if colisiono_right and colisiono_bottom and mi_personaje.esta_saltando:
            for lado in mi_personaje.lados:
                mi_personaje.lados[lado].x += 5
            for lados_agachado in mi_personaje.lados_agachado:
                mi_personaje.lados_agachado[lados_agachado].x +=5

        if colisiono_left and colisiono_bottom and mi_personaje.esta_saltando:
            for lado in mi_personaje.lados:
                mi_personaje.lados[lado].x -= 5
            for lados_agachado in mi_personaje.lados_agachado:
                mi_personaje.lados_agachado[lados_agachado].x -=5
            
        if colisiono_top:
            if mi_personaje.esta_saltando:
                mi_personaje.desplazamiento_y = 2


        if colisiono_right and not mi_personaje.presiono_ctrl:
            if mi_personaje.esta_saltando:
                mi_personaje.desplazamiento_y = 10
            mi_personaje.colision_izquierda_plataforma = True

        if colisiono_left and not mi_personaje.presiono_ctrl:
            if mi_personaje.esta_saltando:
                mi_personaje.desplazamiento_y = 10
            mi_personaje.colision_derecha_plataforma = True
            
        if colisiono_top and not colisiono_top_agachado and mi_personaje.esta_agachado and colisiono_right:
            mi_personaje.colision_izquierda_plataforma = False

        if colisiono_top and not colisiono_top_agachado and mi_personaje.esta_agachado and colisiono_left:
            mi_personaje.colision_derecha_plataforma = False

        if colisiono_top and not colisiono_top_agachado and not mi_personaje.esta_agachado:
            if not colisiono_right and not colisiono_left:
                mi_personaje.esta_agachado = True


        if not colisiono_bottom and not verificar_piso and mi_personaje.esta_saltando:
            mi_personaje.esta_saltando = True

    
        for plataforma_movil in lista_plataformas_movil:
            colisiono_bottom_movil = verificar_colision(mi_personaje.lados["bottom"], plataforma_movil.lados_plataforma["top"])
            colisiono_top_movil= verificar_colision(mi_personaje.lados["top"], plataforma_movil.lados_plataforma["bottom"])
            colisiono_right_movil= verificar_colision(mi_personaje.lados["right"], plataforma_movil.lados_plataforma["left"])
            colisiono_left_movil= verificar_colision(mi_personaje.lados["left"], plataforma_movil.lados_plataforma["right"])


            if colisiono_bottom_movil:
                if mi_personaje.esta_saltando:
                    mi_personaje.esta_saltando = False
                    mi_personaje.potencia_salto = -17
                    ajustar_posicion_jugador(mi_personaje,mi_personaje.lados["bottom"].y,plataforma_movil.lados_plataforma["top"].y)
                    if plataforma.es_tronco:
                        mi_personaje.potencia_salto = -40
                if colisiono_left:
                    empujar_personaje(mi_personaje,30)
                    mi_personaje.esta_saltando = True
                if colisiono_right:
                    empujar_personaje(mi_personaje,-30)
                    mi_personaje.esta_saltando = True

            if colisiono_right_movil and colisiono_bottom_movil:
                mi_personaje.esta_saltando = True
                mi_personaje.desplazamiento_y = 10

            if colisiono_left_movil and colisiono_bottom_movil:
                mi_personaje.esta_saltando = True
                mi_personaje.desplazamiento_y = 10
                
            if colisiono_top_movil:
                if mi_personaje.esta_saltando:
                    mi_personaje.desplazamiento_y = 2

            if colisiono_right_movil:
                if mi_personaje.esta_saltando:
                    empujar_personaje(mi_personaje,-20)
                    mi_personaje.esta_saltando = True
                    mi_personaje.desplazamiento_y = 10
                mi_personaje.colision_izquierda_plataforma = True

            if colisiono_left_movil:
                if mi_personaje.esta_saltando:
                    empujar_personaje(mi_personaje,20)
                    mi_personaje.esta_saltando = True
                    mi_personaje.desplazamiento_y = 10
                mi_personaje.colision_derecha_plataforma = True
            
    

def empujar_personaje(mi_personaje,empuje):
    for lado in mi_personaje.lados:
        mi_personaje.lados[lado].x += empuje
    for lado in mi_personaje.lados_agachado:
        mi_personaje.lados_agachado[lado].x += empuje



def ajustar_posicion_jugador(mi_personaje,posicion_y_pj, posicion_y_plataforma):
        if posicion_y_pj > posicion_y_plataforma:
            diferencia = posicion_y_pj - posicion_y_plataforma
            for lado in mi_personaje.lados:
                mi_personaje.lados[lado].y -= diferencia
            for lado_agachado in mi_personaje.lados_agachado:
                mi_personaje.lados_agachado[lado_agachado].y -= diferencia

        if posicion_y_pj < posicion_y_plataforma:
            diferencia = posicion_y_plataforma - posicion_y_pj
            for lado in mi_personaje.lados:
                mi_personaje.lados[lado].y += diferencia
            for lado_agachado in mi_personaje.lados_agachado:
                mi_personaje.lados_agachado[lado_agachado].y += diferencia

def verificar_colision(rect_1,rect_2):
    return rect_1.colliderect(rect_2)

def colisionar_proyectil_con_enemigo(mi_personaje,lista_enemigos):
    for enemigo in lista_enemigos:
        verificar_proyectil_enemigo = mi_personaje.verificar_colision_proyectil(mi_personaje.lista_proyectiles,enemigo.lados_enemigo["left"],enemigo.lados_enemigo["right"])
        if verificar_proyectil_enemigo:
            enemigo.vida_enemigo = mi_personaje.dañar(enemigo.vida_enemigo)
            enemigo.recibe_daño = True
        if enemigo.vida_enemigo <=0:
            lista_enemigos.remove(enemigo)

def colisionar_proyectil_nave_con_enemigo(mi_personaje_nave,boss):
    verificar_proyectil_enemigo = mi_personaje_nave.verificar_colision_proyectil(mi_personaje_nave.lista_proyectiles,boss.lados["left"],boss.lados["right"])
    if verificar_proyectil_enemigo:
        if not boss.inmunidad:
            boss.vida = mi_personaje_nave.dañar(boss.vida)
            boss.esta_dañado = True
    if boss.vida <=0:
        print("Esta muerto")

def colisionar_proyectil_plataforma(mi_personaje,lista_plataformas):
    for plataforma in lista_plataformas:
        verificar_proyectil_plataformas = mi_personaje.verificar_colision_proyectil(mi_personaje.lista_proyectiles,plataforma.lados_plataforma["left"],plataforma.lados_plataforma["right"])
        if verificar_proyectil_plataformas:
            mi_personaje.colisiono_proyectil_plataforma = True

def colisionar_enemigo_con_personaje(lista_enemigos, mi_personaje, rect_izquierda, rect_derecha, rect_bottom):
    for enemigo in lista_enemigos:
        colisiono_left_con_personaje = verificar_colision(enemigo.lados_enemigo["left"], mi_personaje.lados["right"])
        colisiono_right_con_personaje = verificar_colision(enemigo.lados_enemigo["right"], mi_personaje.lados["left"])
        colisiono_enemigo_con_personaje = enemigo.verificar_colision_enemigo_con_personaje(rect_izquierda, rect_derecha, rect_bottom)
        colisiono_proyectil_enemigo_con_jugador = enemigo.verificar_colision_proyectil_enemigo_con_jugador(rect_izquierda, rect_derecha)
        if colisiono_enemigo_con_personaje or colisiono_proyectil_enemigo_con_jugador:
            tiempo_actual = pygame.time.get_ticks() / 1000
            if tiempo_actual - mi_personaje.tiempo_ultimo_daño >= mi_personaje.tiempo_espera_daño:
                mi_personaje.vida = enemigo.dañar(mi_personaje.vida, 1)
                mi_personaje.recibe_daño = True
                mi_personaje.tiempo_ultimo_daño = tiempo_actual  
        if colisiono_left_con_personaje:
            empujar_personaje(mi_personaje, -20)
        if colisiono_right_con_personaje:
            empujar_personaje(mi_personaje, 20)

def colisionar_boss_con_personaje(boss,mi_personaje,rect_izquierda,rect_derecha,rect_bottom,rect_top):
        colisiono_enemigo_con_personaje = boss.verificar_colision_boss_con_personaje(rect_izquierda,rect_derecha,rect_bottom,rect_top)
        colisiono_proyectil_boss_con_jugador = boss.verificar_colision_proyectil_boss_con_jugador(rect_izquierda,rect_derecha,rect_bottom,rect_top)

        if colisiono_enemigo_con_personaje or colisiono_proyectil_boss_con_jugador:
            tiempo_actual = pygame.time.get_ticks() / 1500
            if tiempo_actual - mi_personaje.tiempo_ultimo_daño >= mi_personaje.tiempo_espera_daño:
                mi_personaje.vida = boss.dañar(mi_personaje.vida,1)
                mi_personaje.recibe_daño = True
                mi_personaje.tiempo_ultimo_daño = tiempo_actual


def colisionar_enemigo_planta_con_personaje(lista_enemigos_planta,mi_personaje,rect_main):
    for enemigo_planta in lista_enemigos_planta:
        verificar_colision_planta = enemigo_planta.verificar_colision_planta(rect_main)
        if verificar_colision_planta:
            enemigo_planta.ataque = True
            mi_personaje.vida = enemigo_planta.dañar(mi_personaje.vida)
            mi_personaje.recibe_daño = True

def colisionar_corazon_con_personaje(lista_corazones,mi_personaje,rectangulo_main):
    for corazon in lista_corazones:
        verificar_colision_corazon = corazon.verificar_colision_corazon(rectangulo_main,mi_personaje.vida)
        if verificar_colision_corazon:
            mi_personaje.vida = corazon.curar(mi_personaje.vida)
            lista_corazones.remove(corazon)
