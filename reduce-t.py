from functools import reduce

def multiply(a, b):
    return a * b

result = reduce(multiply, [1, 2, 3, 4, 5])
print(result)