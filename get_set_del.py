class SomeClass():
    def __init__(self, value):
        self._value = value

    def getvalue(self):
        return self._value

    def setvalue(self, value):
        self._value = value

    def delvalue(self):
        del self._value

    value = property(getvalue, setvalue, delvalue, 'Свойство value')

obj = SomeClass(42)
print(obj.value)
obj.value = 43
print(obj.value)