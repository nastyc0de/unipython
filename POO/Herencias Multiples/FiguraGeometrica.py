from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def setWidth(self, width):
        self._width = width
    
    @property
    def height(self):
        return self._width
    
    @height.setter
    def setWidth(self, height):
        self._height = height
    
    @abstractmethod
    def getArea(self):
        pass
    
    def __str__(self) -> str:
        return f"Figure: {self._height},{self._width}"
    
