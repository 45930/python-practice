from functools import lru_cache
import math

class PrimeIntegers:
    seq = []

    def __init__(self, upto=2**16):
        self.upto = upto
        self.generate_seq(upto)

    
    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, i: int) -> int:
        return self.seq[i]
    
    def generate_seq(self, upto: int) -> int:
        for i in range(upto):
            if PrimeIntegers.is_prime(i):
                self.seq.append(i)

    @staticmethod
    @lru_cache(2**8)
    def is_prime(i: int) -> bool:
        if i <= 1:
            return False
        if i <= 3:
            return True
        if i % 2 == 0 or i % 3 == 0:
            return False
        
        for j in range(5, math.ceil(math.sqrt(i)), 6):
            if i % j == 0 or i % (j + 2) == 0:
                return False
        
        return True

seq = PrimeIntegers(100000)
print(seq[-1])
print(len(seq))
