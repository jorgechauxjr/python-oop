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
profesor = Profesor("Pedor", "101112")

print("Estudiante:")
print(estudiante.solicitar_libro("Python Básico"))
print(estudiante.solicitar_libro("Python Intermedio"))
print(estudiante.solicitar_libro("Python Avanzado"))
print(estudiante.solicitar_libro("Python / DJango")) # Debe indicar límite alcanzado: 3

print()
print("Profesor:")
print(profesor.solicitar_libro("Python Básico"))
print(profesor.solicitar_libro("Python Intermedio"))
print(profesor.solicitar_libro("Python Avanzado"))
print(profesor.solicitar_libro("Python / DJango")) # Todos autorizados
