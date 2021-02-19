class SomeClass:
    def _private(self):
        print('Это внутренний метод объекта')

obj = SomeClass()
obj._private

class SomeClass():
    def __init__(self):
        self.__param = 42

obj = SomeClass()
# obj.__param  =  приведёт к ошибке
obj._SomeClass__param
print(obj._SomeClass__param)