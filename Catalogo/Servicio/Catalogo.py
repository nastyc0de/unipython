import os

class Catalogo:
    path = 'peliculas.txt'

    @classmethod
    def addPelicula(cls, pelicula):
        with open(cls.path, 'a', encoding='utf8') as file:
            file.write(f'{pelicula.name}')
    
    @classmethod
    def listPelicula(cls):
        with open(cls.path, 'r', encoding='utf8') as file:
            print('Catalogo peliculas'.center(50, '-'))
            print(file.read())

    @classmethod
    def deletePelicula(cls):
        os.remove(cls.path)
        print(f'Archivo Eliminado: {cls.path}')