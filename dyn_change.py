class SomeClass(object):
    pass

def squareMethod(self, x):
    return x*x

SomeClass.square = squareMethod
obj = SomeClass()
obj.square(5)
print(obj.square(5))