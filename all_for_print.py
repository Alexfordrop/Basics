print(5,7,9, sep='*', end='@')
print(3, -1, 70, sep='#')

f = open('text.txt', 'w')

f.write('запись от метода write\n')
print('Привет', end='', file=f)

f.close()