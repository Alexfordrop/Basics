import pickle

FIENAME = 'user.dat'

name = 'tom'
age = 19

with open(FIENAME, 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FIENAME, 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print('Имя:', name, '\tВозраст:', age)