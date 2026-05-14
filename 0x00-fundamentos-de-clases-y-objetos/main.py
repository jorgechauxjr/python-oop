class Libro:
    def __init__(self, titulo: str, autor: str, isbn: any, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.contador_prestamos = 0
    
    # metodo que se ejecuta cuando haga print de un objeto libro
    def __str__(self):
        return f"\nLibro: { self.titulo } \nAutor: { self.autor } \nISBN: {self.isbn} \nDisponible: {"Si" if self.disponible else "no"}"
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.contador_prestamos += 1
        return (f"=== El libro '{self.titulo}' fue prestado exitosamente")
    
    def devolver(self):
        self.disponible = True
        return (f"=== El libro '{self.titulo}' fue devuelto y está disponible nuevamente")
    
    def es_popular(self):
        return self.contador_prestamos > 5
    
def obtener_libros_populares(lista_catalogo):
# Filtra y devuelve una nueva lista solo con los libros que cumplen la condición
    return [libro for libro in lista_catalogo if libro.es_popular()]



libro1 = Libro("100 años de soledad", "Gabriel García Marquez", 123, False)
libro2 = Libro("El principito", "Saint-Exupery", 456, True)

# print(libro1.prestar())
# print(libro1.devolver())

catalogo = [libro1, libro2]

# Simulamos 6 préstamos para el libro 1 (Se vuelve popular)
for _ in range(7):
    libro1.prestar()
    libro1.devolver()

# Simulamos solo 2 préstamos para el libro 2 (No es popular)
for i in range(2):
    libro2.prestar()
    libro2.devolver()

# Consultamos los populares del catálogo
populares = obtener_libros_populares(catalogo)

print("--- LIBROS POPULARES EN EL CATÁLOGO ---")
for libro in populares:
    print(f"- {libro.titulo} ({libro.contador_prestamos} préstamos)")