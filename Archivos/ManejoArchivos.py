class ManejoArchivos:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name
    
    def __exit__(self, a,b,c):
        print('Cerramos el recurso'.center(50, '-'))
        if self.name:
            self.name.close()