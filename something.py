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

num = random.randint(1, 100)
'''while True:
    print("Введите число от 1 до 100:")
    num1 = int(input())
    if num1 == num:
        print("Вы угадали!")
        break
    else:
        print("Вы не угадали!")
    if num1 == 1000:
        print("Загаданное число %s" % num)'''

sp1 = ['ауди', 'мазда', 'бмв', 'тойота']
print(random.choice(sp1))

import sys

# in1 = sys.stdin.readline()
#sys.stdout.write(in1)
print(sys.version)

import pickle

game = {'life' : 5, 'armor' : 7, 'level' : 100}
file1 = open('testg.txt', 'wb')
pickle.dump(game, file1)
file1.close()

load_file = open('testg.txt', 'rb')
loaded = pickle.load(load_file)
load_file.close()

print(loaded)