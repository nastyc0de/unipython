from FiguraGeometrica import FiguraGeometrica as FG
from Color import Color

class Rectangulo(FG, Color):
    def __init__(self, width, height, color):
        FG.__init__(self, width, height)
        Color.__init__(self, color)
    
    def getArea(self):
        return self.width * self.height

    def __str__(self):
        return f'{FG.__str__(self)}, {Color.__str__(self)}'
    