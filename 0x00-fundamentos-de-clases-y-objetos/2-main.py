"""
4 ENCAPSULACIÓN EN PYTHON: 
Atributos privados y metodos getter/setter
"""

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: any, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0
    
    # metodo que se ejecuta cuando haga print de un objeto libro
    def __str__(self):
        return f"\nLibro: { self.titulo } \nAutor: { self.autor } \nISBN: {self.isbn} \nDisponible: {"Si" if self.disponible else "no"}"
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return (f"=== El libro '{self.titulo}' fue prestado exitosamente. Total de préstamos: {self.__veces_prestado}")
        return f"'{self.titulo}' no está disponible."
    
    def devolver(self):
        self.disponible = True
        return (f"=== El libro '{self.titulo}' fue devuelto y está disponible nuevamente")
    
    def es_popular(self):
        return self.__veces_prestado > 5
    
    def get_veces_prestado(self):
        return self.__veces_prestado
    
    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado
    
libro1 = Libro("100 años de soledad", "Gabriel García Marquez", 123, True)
libro2 = Libro("El principito", "Saint-Exupery", 456, True)

libro1.set_veces_prestado(10)
print(libro1.get_veces_prestado())

# print(libro1.prestar())
# print(libro1.devolver())

catalogo = [libro1, libro2]
