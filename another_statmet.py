class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

mark = Person('Mark', 25)

mark.is_adult(32)
Person.is_adult(17)

print(mark.is_adult(32))
print(Person.is_adult(17))