from Dominio.Pelicula import Pelicula
from Servicio.Catalogo import Catalogo
option = None
while option != 4:
    try:
        print('''
        Opciones
        1. Agregar Pelicula
        2. Lista Pelicula
        3. Eliminar catalogo
        4. Salir
        ''')
        option = int(input('Escribe tu opcion: (1-4)'))
        if option == 1:
            nombre = input('Ingresa un nombre: ')
            pelicula = Pelicula(nombre)
            Catalogo.addPelicula(pelicula)
        elif option == 2:
            Catalogo.listPelicula()
        elif option == 3:
            Catalogo.deletePelicula()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        option = None

print('Salimos del programa'.center(10, '*'))