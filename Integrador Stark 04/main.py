from functions import *
def stark_marvel_app(lista:list):
    """
    Brief:
    Crea un menu de stark el cual dependendiendo la opcion que ingreso el usuario,llama a la funcion que corresponda.

    Parametro/s:
    Recibe la lista de la cual va a imprimir sus opciones

    Return:
    Nada
    """
    datos_normalizados = False
    seguir = True 
    while seguir:
        respuesta = stark_menu_principal(lista)
        if respuesta <1 or respuesta >6:
            print("ERROR. Elija una opcion de 1 a 7.")
        else:
            if not datos_normalizados and respuesta != 3:
                print("ERROR. Primero se deben normalizar los datos con el punto 3.")
            else:
                match respuesta:
                    case 1:
                        print(imprimir_lista_nombre_iniciales(lista_personajes))
                    case 2:
                        stark_generar_codigo_heroes(lista_personajes)
                    case 3:
                        stark_normalizar_datos(lista_personajes)
                        datos_normalizados = True
                    case 4:
                        stark_imprimir_indice_nombre(lista_personajes)
                    case 5:
                        stark_navegar_fichas(lista_personajes)
                    case 6:
                        seguir = False



stark_marvel_app(menu)