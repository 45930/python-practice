import math
from typing import Self

class Factorial:
    def __iter__(self):
        return self.FactorialIter()

    class FactorialIter:
        def __init__(self) -> None:
            self.i = 0
        
        def __iter__(self) -> Self:
            return self

        def __next__(self) -> int:
            f = math.factorial(self.i)
            self.i += 1
            return f 

factorials = Factorial()

factorials_iter = iter(factorials)

print(next(factorials_iter))
print(next(factorials_iter))
print(next(factorials_iter))
print(next(factorials_iter))
print(next(factorials_iter))
print(next(factorials_iter))
print(next(factorials_iter))