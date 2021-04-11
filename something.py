import copy

class Auto():
    pass

my_auto1 = Auto()
my_auto1.wheels = 4
print(my_auto1.wheels)

my_auto2 = copy.copy(my_auto1)
my_auto2.wheels = 8

print(my_auto1.wheels)
print(my_auto2.wheels)

##

import keyword

print(keyword.iskeyword('if'))
print(keyword.iskeyword('while'))
print(keyword.iskeyword('match'))

##

import random

num =
print(random.randint(1, 100))