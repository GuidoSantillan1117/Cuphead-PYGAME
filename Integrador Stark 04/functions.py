from data_stark import lista_personajes
import re

"""
Brief: Extrae las iniciales de un nombre de heroe.
Funcionamiento: Normaliza el nombre, lo divide en palabras y extrae la primera letra de cada palabra para formar las iniciales. Devuelve las iniciales separadas por puntos o "N/A" si el nombre es vacio.

"""
def extraer_iniciales(nombre_heroe:str):
    lista_iniciales = []
    if len(nombre_heroe)>0: 
        nombre_normalizado = re.sub(r"the|-"," ",nombre_heroe)
        nombre_separado = re.split(r"\s+",nombre_normalizado)
        for nombre in nombre_separado:
            lista_iniciales.append(nombre[0])
        iniciales = ".".join(lista_iniciales)+ "."
    else:
        iniciales = "N/A"

    return iniciales

"""
Brief: Convierte un dato a formato snake_case.
Funcionamiento: Convierte un string a snake_case, reemplazando espacios por guiones bajos y convirtiendo todo a minusculas.

"""
def obtener_dato_formato(dato:str):
    if type(dato) == str:
        convertir_snake_case = re.sub(r"\s+","_",dato)
        validar_mayuscula = re.search(r"[A-Z]",convertir_snake_case)
        if validar_mayuscula != None:
            string_normalizado = convertir_snake_case.lower()
        else:
            string_normalizado = False

    return string_normalizado
"""
Brief: Genera un string con el nombre del heroe en formato snake_case seguido de sus iniciales.
Funcionamiento: Obtiene el nombre en formato snake_case y las iniciales utilizando las funciones obtener_dato_formato y extraer_iniciales.
"""
def stark_imprimir_nombre_con_iniciales(nombre_heroe:dict):
    if type(nombre_heroe) == dict:
        if "nombre" in nombre_heroe:
            nombre = nombre_heroe["nombre"]
            nombre_snake_case = obtener_dato_formato(nombre)
            iniciales_nombre = extraer_iniciales(nombre)
            string_return = f"{nombre_snake_case} ({iniciales_nombre})"
        else:
            string_return = False
    else:
        string_return = False
    return string_return
"""
Brief: Genera una lista de strings con nombres en formato snake_case seguidos de iniciales.
Funcionamiento: Itera sobre la lista de heroes, utiliza stark_imprimir_nombre_con_iniciales y agrega los resultados a una lista.
"""
def imprimir_lista_nombre_iniciales(lista:list):
    lista_nombres_iniciales = []
    if type(lista) == list:
        if len(lista)>0:
            for personaje in lista:
                nombre_iniciales = stark_imprimir_nombre_con_iniciales(personaje)
                lista_nombres_iniciales.append(nombre_iniciales)
        else:
            lista_nombres_iniciales = False
        
    else:
        lista_nombres_iniciales = False
        
    return lista_nombres_iniciales

"""
Brief: Genera un codigo unico para un heroe.
Funcionamiento: Utiliza el genero del heroe y un ID para generar un codigo unico.
"""
def generar_codigo_heroe(diccionario:dict,id:int):
    genero = diccionario["genero"]
    if len(genero)>0:
        if "M" in genero or "F" in genero or "NB" in genero:
            match genero:
                case "M":
                    inicial_genero = 1
                case "F":
                    inicial_genero = 2
                case "NB":
                    inicial_genero = 0

            string_codigo = f"{genero}-{inicial_genero}"
            id_casteado = str(id)

            fill_id = id_casteado.zfill(10-len(string_codigo))
            string_codigo_final = string_codigo + fill_id
        else:
            string_codigo_final = "N/A"
    else:
        string_codigo_final = "N/A"

    return string_codigo_final
"""
Brief: Genera y muestra codigos para la lista de heroes
Funcionamiento: Itera sobre la lista de heroes, utiliza generar_codigo_heroe y muestra los codigos junto con los nombres.
"""
def stark_generar_codigo_heroes(lista:list):
    if len(lista)>0:
        contador = 0
        id = 0
        for personaje in lista:
            if type(personaje) == dict:
                id += 1
                codigo = generar_codigo_heroe(personaje,id)
                nombre_con_inicial = imprimir_lista_nombre_iniciales(lista)[contador]

                print(f"*{nombre_con_inicial}| {codigo}")

                contador+=1

            else:
                return False
        print(f"Se generaron {id} códigos.")
    else:
        return False
"""
Brief: Elimina espacios al principio y al final de un string.
Funcionamiento: Utiliza el metodo strip para eliminar espacios en blanco al principio y al final de un string.
"""        
def sacar_espacios(numero:str):
    numero_sin_espacios = numero.strip()
    return numero_sin_espacios
"""
Brief: Convierte un string a entero y maneja casos especiales.
Funcionamiento: Utiliza expresiones regulares para verificar y convertir un string a entero. Retorna un valor especial para casos especiales como negativos y caracteres no numericos.
"""        
def sanitizar_entero(numero_str:str):
    numero_sin_espacios = sacar_espacios(numero_str)
    if re.match(r"^\d+$",numero_sin_espacios):
        numero_string = int(numero_sin_espacios)

    elif re.match(r"^-\d+$",numero_sin_espacios):
        numero_string = -2
    elif re.match(r"[^0-9-]",numero_sin_espacios):
        numero_string = -1
    else:
        numero_string = -3

    return numero_string

"""
Brief: Convierte un string a flotante y maneja casos especiales.
Funcionamiento: Utiliza expresiones regulares para verificar y convertir un string a flotante. Retorna un valor especial para casos especiales como negativos y caracteres no numericos.
"""
def sanitizar_flotante(numero_str:str):
    flotante_sin_espacios = sacar_espacios(numero_str)
    if re.match(r'^\d+\.\d+$',flotante_sin_espacios):
        numero_float = float(flotante_sin_espacios)
    elif re.match(r'^-\d+\.\d+$',flotante_sin_espacios):
        numero_float = -2
    elif re.search(r'[^0-9.-]',flotante_sin_espacios):
        numero_float = -1
    else:
        numero_float = -3


    return numero_float

"""
Brief: Normaliza un string y maneja casos especiales.
Funcionamiento: Verifica y normaliza un string, reemplazando espacios por guiones bajos, convirtiendo a minusculas y manejando casos especiales.
"""
def sanitizar_string(valor_str:str,valor_por_defecto = "-"):
    if len(valor_str) == 0 and len(valor_por_defecto)>0:
        string_con_espacios = valor_por_defecto.lower()
        string = string_con_espacios.strip()

    else:
        verificar_string = re.search(r"[0-9]",valor_str)
        verificar_barra = re.search(r"/",valor_str)
        if verificar_string:
            string = "N/A"
        else:
            if verificar_barra:
                string_con_espacios = re.sub(r"/"," ",valor_str)
                string_con_espacios_minusculas = string_con_espacios.lower()
                string = string_con_espacios_minusculas.strip()
            else:
                string = valor_str.lower()

    return string
"""
Brief: Normaliza un dato específico de un héroe.
Funcionamiento: Verifica y normaliza un dato específico de un héroe según el tipo de dato especificado.
"""
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
    estado = True
    tipo_dato_minuscula = tipo_dato.lower()
    lista_tipo_dato = ["string","flotante","entero"]

    if tipo_dato_minuscula not in lista_tipo_dato: 
        print("Tipo de dato No reconocido")
        estado = False
    if clave not in heroe:
        print("La clave especificada no existe en el heroe.")
        estado = False

    if tipo_dato == "string":
        heroe[clave] = sanitizar_string(heroe[clave])
    elif tipo_dato == "flotante":
        heroe[clave] = sanitizar_flotante(heroe[clave])
    elif tipo_dato == "entero":
        heroe[clave] = sanitizar_entero(heroe[clave])

    return estado
"""
Brief: Normaliza los datos de la lista de heroes.
Funcionamiento: Itera sobre la lista de heroes y utiliza la función sanitizar_dato para normalizar distintos tipos de datos.
"""
def stark_normalizar_datos(lista_heroes:list):
    if len(lista_heroes)>0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe,"altura","Flotante") 
            sanitizar_dato(heroe,"peso","Flotante")
            sanitizar_dato(heroe,"color_ojos","String")
            sanitizar_dato(heroe,"color_pelo","String") 
            sanitizar_dato(heroe,"fuerza","Flotante")
            sanitizar_dato(heroe,"inteligencia","Entero")   
        print("Datos normalizados.")
    else:
        print("Error: Lista de heroes vacia")
"""
Brief: Imprime nombres de heroes normalizados.
Funcionamiento: Itera sobre la lista de héroes, normaliza los nombres y los imprime en formato snake_case.
"""
def stark_imprimir_indice_nombre(lista_heroes:list):
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            nombre = heroe["nombre"]
            nombre_sin_espacios = nombre.strip()
            nombre_normalizado = nombre_sin_espacios.replace("the", " ")
            nombre_final = re.sub(r'\s+', '-', nombre_normalizado)

            print(nombre_final)
    else:
        print("Lista de héroes vacía")
"""
Brief: Genera un string de separacion.
Funcionamiento: Genera un string de separación con un patron y un largo especificados. Puede imprimirlo o devolverlo según el parametro imprimir.
"""
def generar_separador(patron:str,largo:int, imprimir: bool = True):
    if len(patron)>0 and len(patron)<=2 and largo>=1 and largo<=235:
        string_generado = patron * largo
        if imprimir:
            print(string_generado)

    else:
        string_generado = "N/A"

    return string_generado
"""
Brief: Genera un string de encabezado.
Funcionamiento: Convierte un titulo a mayúsculas y utiliza generar_separador para generar un encabezado.
"""
def generar_encabezado(titulo:str):
    titulo_mayusucla = titulo.upper()
    separador = generar_separador("*",120,False)
    string_encabezado = f"{separador}\n{titulo_mayusucla}\n{separador}"
    return string_encabezado
"""
Brief: Genera y devuelve un string con informacion detallada de un heroe.
Funcionamiento: Utiliza funciones auxiliares para formatear y mostrar la informacion detallada de un heroe.
"""
def imprimir_ficha_heroe(heroe:dict,id):
    encabezado_principal = generar_encabezado("PRINCIPAL")
    nombre_con_iniciales = stark_imprimir_nombre_con_iniciales(heroe)
    identidad_secreta = obtener_dato_formato(heroe["identidad"])
    consultora = obtener_dato_formato(heroe["empresa"])
    codigo_heroe = generar_codigo_heroe(heroe,id)
    string_info_principal = f"{encabezado_principal}\n\tNOMBRE DEL HEROE:\t\t {nombre_con_iniciales}\n\tIDENTIDAD SECRETA:\t\t{identidad_secreta}\n\tCONSULTORA:\t\t\t{consultora}\n\tCODIGO DE HEROE:\t\t{codigo_heroe}"
    encabezado_fisico = generar_encabezado("FISICO")
    altura = "{:.2f}".format(float(heroe["altura"]))
    peso = "{:.2f}".format(float(heroe["peso"]))
    fuerza = heroe["fuerza"]

    string_info_fisico = f"{encabezado_fisico}\n\tALTURA:\t\t{altura} cm.\n\tPESO:\t\t{peso} kg.\n\tFUERZA:\t\t{fuerza} N"
    encabezado_señas = generar_encabezado("SEÑAS PARTICULARES")
    color_ojos = heroe["color_ojos"]
    color_pelo = heroe["color_pelo"]
    string_info_señas = f"{encabezado_señas}\n\tCOLOR DE OJOS:\t\t{color_ojos}\n\tCOLOR DE PELO:\t\t{color_pelo}"


    string_principal = f"{string_info_principal}\n{string_info_fisico}\n{string_info_señas}"
    return string_principal
"""
Brief: Navega entre las fichas  de heroes de la lista.
Funcionamiento: Muestra informacion detallada de heroes en una lista permitiendo navegar entre ellos.
"""
def stark_navegar_fichas(lista_heroes):
    if len(lista_heroes)<0:
        print("La lista de héroes está vacía.")
        return

    indice_actual = 0

    while True:
        print(imprimir_ficha_heroe(lista_heroes[indice_actual],indice_actual+1))

        opcion = input("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ 3 ] Salir\nIngrese su opción: ")

        if opcion == '1':
            indice_actual = (indice_actual - 1)
            if indice_actual == -1 :
                indice_actual = 23
        elif opcion == '2':
            indice_actual = (indice_actual + 1)
            if indice_actual == 24 :
                indice_actual = 0
        elif opcion == '3':
            print("Salio del menu")
            break
        else:
            print("Ingrese una opción valida")





menu = ["--------------------------------------------------------------------------------------\n\t\t\t\t MENU PRINCIPAL\n--------------------------------------------------------------------------------------",
        "1 - Imprimir la lista de nombres junto con sus iniciales","2 -Imprimir la lista de nombres y el código del mismo",
        "3 - Normalizar datos","4 - Imprimir índice de nombres", "5 - Navegar fichas","\n6.Salir"]



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

        

        



        



