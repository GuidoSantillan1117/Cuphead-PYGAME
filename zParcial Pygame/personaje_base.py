from proyectil import Proyectil
class PersonajeBaseConProyectiles:
    def __init__(self) -> None:
        self.lista_proyectiles = []
        
    def dibujar_listas_proyectiles(self, pantalla, lista, velocidad):
        for proyectil in lista:
            proyectil.animar_proyectil(pantalla)
            proyectil.trayecto_proyectil(velocidad)
                
    def update_proyectiles(self, pantalla, velocidad):
        self.dibujar_listas_proyectiles(pantalla, self.lista_proyectiles, velocidad)

    def verificar_colision_proyectil(self,lista,rectangulo_izquierda,rectangulo_derecha):
        colisiono = False
        for proyectil in lista:
            if proyectil.lados_proyectil["main"].colliderect(rectangulo_izquierda) or proyectil.lados_proyectil["main"].colliderect(rectangulo_derecha):
                lista.remove(proyectil)
                colisiono = True
        return colisiono