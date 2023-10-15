import numbers

class Point:
    def __init__(self, x: numbers.Real, y: numbers.Real):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
            self.tuple = (x, y)
        else:
            raise TypeError("x and y must be real numbers")

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"
    
    def __len__(self) -> int:
        return len(self.tuple)
    
    def __getitem__(self, i: int) -> int:
        return self.tuple[i]