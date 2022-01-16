
from abc import ABC, abstractmethod


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calculationArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calculationArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{ \"Circle\": {str(self.calculationArea())} }}"


c = Circle(10)
print(c.calculationArea())
print(c.toJSON())