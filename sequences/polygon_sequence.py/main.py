from Point import Point
from PolygonSequence import PolygonSequence

a = Point(1, 2)
b = PolygonSequence(a, (2, 2))

print(b)

b += a

print(b)

b.extend(b)

print(b)

b.insert(2, (10, 20))

print(b)

b[1] = Point(2, 3)
b[1] = (0,0)

print(b)
print(b.pop(1))
print(sorted(b, key=lambda pt: pt.tuple))

b.sort()
print(b)

for p in b:
    print(p)
