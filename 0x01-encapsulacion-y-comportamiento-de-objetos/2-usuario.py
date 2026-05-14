from typing import Protocol

class SolicitanteProtocol (Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...

    

class Usuario:    
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"La solicitud del libro '{titulo}' fue realizada exitosamente"

class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Prestamoo del libro '{titulo}' autorizado."
        else:
            return f"No puedes prestar mas libros, límite alcanzado: {self.limite_libros}"

class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamoo del libro '{titulo}' autorizado."

estudiante = Estudiante("Juan", "123456789", "Ing. Sistemas")
estudiante1 = Estudiante("Jose", "654", "Medicina")
profesor = Profesor("Pedor", "101112")

# tipado. Usuarios es una lista de tipo Solicitante Protocol
usuarios: list[SolicitanteProtocol] = [estudiante, estudiante1, profesor]

# cada usuario se le autoriza prestar el libro
# estudiante, estudiante1 y profesor
for usuario in usuarios:
    print(usuario.solicitar_libro("Titulo de ejemplo"))
