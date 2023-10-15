from Point import Point
from typing import Self, Iterable

class PolygonSequence:
    def __init__(self, *points: tuple[Point] | Iterable[int]):
        if points:
            self.points = [Point(*point) for point in points]
        else:
            self.points = []
    
    def __repr__(self) -> str:
        return f"Polygon({self.points})"
    
    def __len__(self) -> int:
        return len(self.points)
    
    def __getitem__(self, i: int) -> Point:
        return self.points[i]
    
    def __setitem__(self, i: int | slice, value: Self | Point | Iterable[int]) -> None:
        try:
            [Point(*point) for point in value]
            is_point = False
        except TypeError:
            try:
                Point(*value)
                is_point = True
            except TypeError:
                raise TypeError("Value must be a point or an iterable of points")
        
        if isinstance(i, int) and is_point:
            # we expect that value is one point
            p = Point(*value)
            self.points[i] = p
        elif isinstance(i, slice) and not is_point:
            # we expect that value is many points
            points = [Point(*p) for p in value]
            self.points[i] = points
        else:
            raise TypeError("Incompatible inputs.  Must use a slice and iterable of points, or an int and a point")
    
    def __add__(self, other: Self | Point | Iterable[int]) -> Self:
        if isinstance(other, PolygonSequence):
            new_points = self.points + other.points
            return PolygonSequence(*new_points)
        else:
            new_points = self.points + [Point(*other)]
            return self
    
    def append(self, point: Point) -> None:
        self.points.append(Point(*point))
    
    def insert(self, i: int, point: Point | Iterable[int]) -> None:
        self.points.insert(i, Point(*point))
    
    def extend(self, other: Self | Iterable[int]) -> None:
        if isinstance(other, PolygonSequence):
            self.points.extend(other.points)
        else:
            self.points.append(Point(*other))
    
    def __iadd__(self, other: Self | Point | Iterable[int]) -> Self:
        self.extend(other)
        return self
    
    def __delitem__(self, i: int | slice):
        del self.points[i]
    
    def pop(self, i: int) -> Point:
        return self.points.pop(i)
    
    def sort(self, reverse=False) -> Self:
        self.points.sort(key=lambda pt: pt.tuple, reverse=reverse)