from data_stark import *
import regex
import json
"""
Brief: Lee el contenido de un archivo y lo devuelve como texto.
Funcionamiento: Abre el archivo especificado en modo lectura, lee su contenido y lo devuelve como una cadena de texto.
"""

def leer_archivo(nombre_archivo:str):
    try:
        with open(nombre_archivo,"r",encoding='utf-8') as archivo:
            texto_contenido = archivo.read()
    except FileNotFoundError:
        print("Error, no se encontro el nombre del archivo.")
        texto_contenido = None
    except Exception as e:
        print(f"Error inesperado: {e}")
        texto_contenido = None

    return texto_contenido


"""
Brief: Guarda el contenido en un archivo.
Funcionamiento: Abre el archivo especificado en modo escritura, escribe el contenido y devuelve un booleano de si se creo o no.
"""
def guardar_archivo(nombre_archivo,contenido):
    try:
        with open(nombre_archivo,"w",encoding='utf-8') as archivo:
            archivo.write(contenido)
            archivo_creado = True
        print(f"Se creo con exito el archivo: {nombre_archivo}")
    except ValueError:
        print(f"Error: No se pudo crear el archivo {nombre_archivo}. Verifica el nombre y la extensión.")
        archivo_creado = False
    except Exception as e:
        print(f"Error inesperado al crear el archivo {nombre_archivo}: {e}")
        archivo_creado = False

    return archivo_creado

"""
Brief: Normaliza los datos numéricos en una lista de héroes.
Funcionamiento: Itera sobre la lista de heroes y convierte las alturas y pesos a float y la fuerza a int
"""
def normalizar_datos(lista_heroes):
    for heroe in lista_heroes:
        if type(heroe["altura"]) != float:
            heroe["altura"] = float(heroe["altura"])
        if type(heroe["peso"]) != float:
            heroe["peso"] = float(heroe["peso"])
        if type(heroe["fuerza"]) != int:
            heroe["fuerza"] = int(heroe["fuerza"])


"""
Brief: Genera un archivo CSV con los datos de la lista de heroes.
Funcionamiento: Crea un string CSV con los datos de la lista de heroes y guarda ese string en un archivo.
"""
def generar_csv(nombre_archivo,lista_heroes):
    if not lista_heroes:
        print("La lista de heroes esta vacia")
        return False

    string_csv = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"

    for heroe in lista_heroes:
        nombre = heroe.get("nombre", "")
        identidad = heroe.get("identidad", "")
        empresa = heroe.get("empresa", "")
        altura = heroe.get("altura", "")
        peso = heroe.get("peso", "")
        genero = heroe.get("genero", "")
        color_ojos = heroe.get("color_ojos", "")
        color_pelo = heroe.get("color_pelo", "")
        fuerza = heroe.get("fuerza", "")
        inteligencia = heroe.get("inteligencia", "")

        string_valores= f"{nombre},{identidad},{empresa},{altura},{peso},{genero},{color_ojos},{color_pelo},{fuerza},{inteligencia}\n"
        string_csv+= string_valores
        
    guardar_archivo(nombre_archivo,string_csv)

"""
Brief: Lee un archivo CSV y devuelve una lista de diccionarios.
Funcionamiento: Lee las líneas del archivo CSV, extrae las claves, y crea una lista de diccionarios con los valores de cada línea. Convierte las claves "altura", "peso" y "fuerza" a números.
"""
def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        lista_heroes = False
        print("Error, no se encontró el nombre del archivo.")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        lista_heroes = False
        return None

    claves = lineas[0].strip().split(",")

    lista_heroes = []

    for linea in lineas[1:]:
        heroes = {}
        valores = linea.strip().split(",")
        for i in range(0, 9):
            clave = claves[i]
            valor = valores[i]
            if clave in ["altura", "peso", "fuerza"]:
                valor = float(valor)  # Convertir a número si es una de las claves numéricas
            heroes[clave] = valor
        lista_heroes.append(heroes)

    return lista_heroes


# a = leer_csv("heroes.csv")
# print(a)


"""
Brief: Genera un archivo JSON con los datos de la lista de heroes.
Funcionamiento: Crea un diccionario con la lista de heroes y guarda ese diccionario en un archivo JSON.
"""
def generar_json(nombre_archivo,lista_heroes,nombre_lista):
    if lista_heroes:
        diccionario = {nombre_lista:lista_heroes}

    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(diccionario, archivo, ensure_ascii=False, indent=4)

import json
"""
Brief: Lee un archivo JSON y devuelve una lista de heroes.
Funcionamiento: Lee el archivo JSON, obtiene la lista de heroes y la devuelve.
"""
def leer_json(nombre_archivo, nombre_lista):
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            data_json = json.load(archivo)
            lista_obtenida = data_json.get(nombre_lista)

        if lista_obtenida:
            return lista_obtenida
        else:
            print("Error,lista vacia")
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo {nombre_archivo}")
        return False
    except Exception as e:
        print(f"Error inesperado al leer el archivo {nombre_archivo}: {e}")
        return False
"""
Brief: Ordena la lista de heroes por una clave en orden ascendente.
Funcionamiento: Ordena la lista de heroes según el valor de la clave en orden ascendente.
"""
def ordenar_clave_ascendente(lista_heroes,clave):
    lista_claves_posibles = ["altura","peso","fuerza"]
    if clave in lista_claves_posibles:
        for i in range(len(lista_heroes)-1):
            for j in range(i+1,len(lista_heroes)):
                if(lista_heroes[i][clave] > lista_heroes[j][clave]):
                    aux = lista_heroes[i]
                    lista_heroes[i] = lista_heroes[j]
                    lista_heroes[j] = aux
        return lista_heroes
    else:
        print("Clave inexistente")
"""
Brief: Ordena una la lista de heroes por una clave en orden descendente.
Funcionamiento: Ordena la lista de heroes según el valor de la clave  en orden descendente.
"""
def ordenar_clave_descendente(lista_heroes,clave):
    lista_claves_posibles = ["altura","peso","fuerza"]
    if clave in lista_claves_posibles:
        for i in range(len(lista_heroes)-1):
            for j in range(i+1,len(lista_heroes)):
                if(lista_heroes[i][clave] < lista_heroes[j][clave]):
                    aux = lista_heroes[i]
                    lista_heroes[i] = lista_heroes[j]
                    lista_heroes[j] = aux
        return lista_heroes
    else:
        print("Clave inexistente")

"""
Brief: Ordena la lista por una clave en el orden especificado.
Funcionamiento: Llama a las funciones ordenar_clave_ascendente o ordenar_clave_descendente segun la clave y el orden especificados.
"""
def ordenar_lista(lista,clave,orden):
    ordenes_posible = ["asc","desc"]
    if orden in ordenes_posible:
        if orden == ordenes_posible[0]:
            lista_ordenada = ordenar_clave_ascendente(lista,clave)
        elif orden == ordenes_posible[1]:
            lista_ordenada = ordenar_clave_descendente(lista,clave)
        print(lista_ordenada)
    else:
        print("Orden invalido.")


"""
Brief: Lista los heroes ordenados por altura desde un archivo CSV.
Funcionamiento: Lee el archivo CSV, convierte las alturas a int y ordena la lista por altura en orden ascendente.
"""
def listar_heroes_por_altura_csv(nombre_csv):
    lista_personajes_csv = leer_csv(nombre_csv)
    if lista_personajes_csv:
        ordenar_clave_ascendente(lista_personajes_csv, "altura")
        return lista_personajes_csv
    else:
        print("Error: La lista está vacía o hay un problema con el archivo CSV")


"""
Brief: Lista los heroes ordenados por peso desde un archivo JSON.
Funcionamiento: Lee el archivo JSON y ordena la lista por peso en orden descendente.
"""
def listar_heroes_por_peso_json(nombre_json):
    lista_personajes_json = leer_json(nombre_json, "heroes")
    if lista_personajes_json:
        ordenar_clave_descendente(lista_personajes_json,"peso")
        return lista_personajes_json

    else:
        print("Error: La lista esta vacia,verifica el archivo JSON")

"""
Brief: Lista los héroes ordenados por fuerza.
Funcionamiento: Ordena la lista en forma ascendente o descendente segun el ingreso del usuario.
"""

def ordenar_lista_fuerza(lista_heroes,orden):
    ordenar_lista(lista_heroes,"fuerza",orden)



menu = ["--------------------------------------------------------------------------------------\n\t\t\t\t MENU PRINCIPAL\n--------------------------------------------------------------------------------------",
        "1-Normalizar datos","2-Generar CSV", "3-Listar heroes del archivo CSV ordenados por altura ASC","4-Generar JSON", "5-Listar heroes del archivo JSON ordenados por peso DESC","6-Ordenar Lista por fuerza","\n7.Salir"]



def imprimir_menu(menu:list):
    """
    Brief:
    Imprime cada una de las opciones de un menu.

    Parametro/s:
    Recibe el menu con sus opciones.

    Return:
    Nada
    """
    for opcion in menu:
        print(opcion)

def validar_entero(numero:str):
    """
    Brief:
    Valida si el numero ingresado es entero.

    Parametro/s:
    Recibe el numero el cual valida.

    Return:
    Devuelve True si es un digito y False en caso de no serlo
    """
    return numero.isdigit()

def stark_menu_principal(lista:list):
    """
    Brief:
    Imprime en pantalla el menu con las opciones y le pide al usuario que ingrese un numero que sera verificado por la funcion anterior 

    Parametro/s:
    Recibe el menu del cual va a imprimir sus opciones

    Return:
    Si el usuario ingreso un digito,devuelve su valor,si no, devuelve False
    """
    imprimir_menu(lista)
    respuesta = (input("\nIngrese una opcion: "))
    if validar_entero(respuesta):
        return int(respuesta)
    else:
        return False




