class Person:
    name = 'Tom'

    def person_info(self):
        print("Привет, меня зовут", self.name)

person1 = Person()
person1.person_info()

person2 = Person()
person2.name = "Sam"
person2.person_info()