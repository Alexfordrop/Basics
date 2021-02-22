class Parent:
    def __init__(sels):
        print('Parent init')

    def method(self):
        print('Parent method')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def method(self):
        super(Child, self).method()

child = Child()
child.method()