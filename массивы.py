arr_a = [34, 65, 2345, 'hi', 'bee']
for i in range(len(arr_a)):
    print(arr_a[i])

print(arr_a[3])

print('Длина массива: ', len(arr_a))

arr_b = [34, 756, 44]
arr_a.extend(arr_b)

for i in range(len(arr_a)):
    print(arr_a[i])

print('Длина массива: ', len(arr_a))

arr_c = arr_a + arr_b
for i in range(len(arr_c)):
    print(arr_c[i])

print('Длина массива: ', len(arr_c))