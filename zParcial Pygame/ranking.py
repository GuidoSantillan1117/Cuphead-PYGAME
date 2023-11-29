import sqlite3


# def crear_tabla():
# 	with sqlite3.connect("C:/Users/guido/OneDrive/Escritorio/4.db") as conexion:
# 		try:
# 			sentencia = ''' create  table puntaje
# 			(
# 			id integer primary key autoincrement,
# 			nombre text not null,
# 			score int

# 			)
# 			'''
# 			conexion.execute(sentencia)
# 			print("Se creo la tabla de ranking")                       
# 		except sqlite3.OperationalError:
# 			print("La tabla de ranking ya existe")


	#INSERT:
def agregar_valores_tabla(nombre,score):
	with sqlite3.connect("C:/Users/guido/OneDrive/Escritorio/4.db") as conexion:
		try:
			conexion.execute("insert into puntaje(nombre,score) values (?,?)", (nombre,score))
			conexion.commit()
		except:
			print("Error")



def obtener_valores_tabla():
	lista_datos = []
	with sqlite3.connect("C:/Users/guido/OneDrive/Escritorio/4.db") as conexion:
		cursor=conexion.execute("SELECT * FROM puntaje order by score DESC LIMIT 5")
		for fila in cursor:
			lista_datos.append(fila)

	return lista_datos