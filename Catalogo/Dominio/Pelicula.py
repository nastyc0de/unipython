class Pelicula:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def setName(self, name):
        self._name = name

    def __str__(self):
        return f'Pelicula {self.name}'