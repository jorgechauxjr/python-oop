class Libro:
    def __init__(self, titulo: str, autor: str, isbn: any, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    catalogo = []

libro1 = Libro("100 años de soledad", "Gabriel García Marquez", 123, False)
libro2 = Libro("El principito", "Saint-Exupery", 456, True)

# print(f"Libro: { libro1.titulo } \nAutor: { libro1.autor } \nISBN: {libro1.isbn} \nDisponible: {"Si" if libro1.disponible else "no"}")
# print()
# print(f"Libro: { libro2.titulo } \nAutor: { libro2.autor }\nISBN: {libro2.isbn} \nDisponible: {"Si" if libro2.disponible else "no"}")

catalogo = [libro1, libro2]

for libro in catalogo:
    print(f"Libro: { libro.titulo } \nAutor: { libro.autor } \nISBN: {libro.isbn} \nDisponible: {"Si" if libro.disponible else "no"}")
    print()
