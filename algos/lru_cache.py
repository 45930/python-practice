class LRUCache:
    __slots__ = ("capacity", "values")

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}

    def get(self, key: int) -> int:
        if key in self.values:
            self.values[key] = self.values.pop(key)
        return self.values.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                oldest_key = list(self.values.keys())[0]
                del self.values[oldest_key]
        else:
            self.values.pop(key)
        self.values[key] = value


c = LRUCache(4)

c.put(1, 10)
c.put(2, 20)
c.put(3, 40)
c.get(1)
c.put(4, 40)
c.put(5, 50)

print(c.values)
