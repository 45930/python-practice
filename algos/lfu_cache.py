class LFUCache:
    __slots__ = ("capacity", "values", "counters", "min_freq")

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {1: {}}  # freq -> { key -> value}
        self.counters = {}  # { key -> freq }
        self.min_freq = 1

    def _get_value(self, key: int) -> int:
        frequency = self.counters[key]
        values = self.values[frequency]
        return values[key]

    def _set_value(self, key: int, value: int) -> int:
        self.values[self.counters[key]][key] = value

    def update_frequency(self, key: int) -> None:
        freq = self.counters[key]
        value = self.values[freq].pop(key)
        if freq == self.min_freq and len(self.values[freq]) == 0:
            self.min_freq += 1
        if freq + 1 not in self.values:
            self.values[freq + 1] = {}
        self.counters[key] = freq + 1
        self.values[freq + 1].update({key: value})

    def get(self, key: int) -> int:
        print(f"Get {key}")
        if key not in self.counters:
            return -1

        self.update_frequency(key)
        return self._get_value(key)

    def put(self, key: int, value: int) -> None:
        print(f"Put {key}")
        if key in self.counters:
            self.update_frequency(key)
            self._set_value(key, value)
        else:
            if len(self.counters) == self.capacity:
                lfu_key = list(self.values[self.min_freq].keys())[0]
                self.values[self.min_freq].pop(lfu_key)
                self.counters.pop(lfu_key)
            self.counters[key] = 1
            self.values[1].update({key: value})
            self.min_freq = 1


c = LFUCache(3)


c.put(2, 2)
c.put(1, 1)
c.get(2)
c.get(1)
c.get(2)
c.put(3, 3)
c.put(2, 3)
c.put(3, 2)
c.put(4, 4)

print(c.values)
print(c.counters)
print(c.min_freq)
