class Someclass(object):
    attr1 = 42

    def method1(self, x):
        return 2*x

obj = Someclass()
obj.method1(6)
obj.attr1

print(obj.attr1)
print(obj.method1(6))