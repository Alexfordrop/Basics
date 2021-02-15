class SomeClass(object):
    @classmethod
    def hello(cls):
        print('Привет, всем!'.format(cls.__name__))

SomeClass.hello()