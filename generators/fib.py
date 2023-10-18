def fib():
    x = 0
    y = 1
    yield 1
    while True:
        yield x + y
        x, y = y, x + y


fibgen = fib()
print(next(fibgen))
print(next(fibgen))
print(next(fibgen))
print(next(fibgen))
print(next(fibgen))
print(next(fibgen))
