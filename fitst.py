from itertools import islice

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

slice = list(islice(fib(), 6))
print(slice)