class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        assert value > 0, 'Age cannot be negative.'
        self.__age = value

mark = Person('Mark', 25)
mark.age = 30

print(mark.age)

mark.age = -20