import json
from datetime import datetime

class Persistencia:
    """
    Esta clase nos permite manejar el archivo en donde vamos a guardar todos nuestros datos
    """
    def __init__(self, archivo="biblioteca.json") -> None:
        self.archivo = archivo

    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [usuario.__dict__ for usuario in biblioteca.usuarios],
            "libros": [libro.__dict__ for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().isoformat(),
        }
        with open(self.archivo, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)