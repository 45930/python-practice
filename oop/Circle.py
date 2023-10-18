from numbers import Real
from timeit import timeit
import math


class Circle:
    def __init__(self, r: Real) -> None:
        self._r = r
        self._area = None

    @property
    def radius(self) -> Real:
        return self._r

    @radius.setter
    def radius(self, r: Real):
        self._r = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius**2
        return self._area


c = Circle(4)
print(c.area)

c.radius = 3
print(c.area)
