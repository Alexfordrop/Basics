class Multiplier:
    def __call__(self, x, y):
        return x*y

multiply = Multiplier()
multiply(19, 19)

multiply.__call__(19, 19)

print(multiply(19, 19))
print(multiply.__call__(19, 19))