
from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calculationArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calculationArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calculationArea(self):
        return self.side * self.side


#g = GraphicShape()

c = Circle(10)
print(c.calculationArea())
s = Square(12)
print(s.calculationArea())