from FiguraGeometrica import FiguraGeometrica as FG
from Color import Color

class Cuadrado(FG, Color):
    def __init__(self, width, color):
        FG.__init__(self, width, width)
        Color.__init__(self, color)
    def getArea(self):
        return self.width ** 2
    def __str__(self):
        return f'{FG.__str__(self)}, {Color.__str__(self)}'