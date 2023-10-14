from functools import lru_cache
import math

class PrimeIntegers:
    def __init__(self, n = 1000):
        self.n = n
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, i: int) -> int:
        if i < 0:
            i = self.n + i
        if i < 0 or i >= self.n:
            raise IndexError
        else:
            return PrimeIntegers.ith_prime(i)


    @staticmethod
    @lru_cache(2**16)
    def ith_prime(i: int) -> int:
        if i == 0:
            return 2
        if i == 1:
            return 3

        ## fill the cache
        for j in range(i):
            PrimeIntegers.ith_prime(j)
        
        ## Then search
        j = PrimeIntegers.ith_prime(i - 1) + 2
        while True:
            if PrimeIntegers.is_prime(j):
                return j
            j += 1

    @staticmethod
    @lru_cache(2**16)
    def is_prime(i: int) -> bool:
        if i <= 1:
            return False
        if i <= 3:
            return True
        if i % 2 == 0 or i % 3 == 0:
            return False
        
        for j in range(5, math.ceil(math.sqrt(i)), 2):
            if i % j == 0 or i % (j + 2) == 0:
                return False
        
        return True

seq = PrimeIntegers(10000)
print(seq[0])
print(seq[-1])
print(len(seq))