ii = 0
array_y = [1, 2, 3, 9, 8, 7, 0]
while ii < 7:
    print("array_y[",ii,"] : ", array_y[ii])
    ii = ii + 1

print("---------")


for i in range(0, 6):
    print(i)

array_a = ['one', 'two', 'three', 'some', 'any']
for i in array_a:
    print(i)

array_b = [-4, 6, 8, -3, 0, 2, 100, -20]
for i in array_b:
    if i > 0:
        print(i)

array_c = [5, 7, 2, 4, 0, -2, -4, -7, 77, 90, -30]
for i in array_c:
    if i == 77:
        print('Нашли 77')
        break
    print(i)
else:
    print('Не нашли 77')
