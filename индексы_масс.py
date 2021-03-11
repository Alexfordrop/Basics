arr = [23, 56, 33, 44, 88, 65, 11]
print(arr[0])
print(arr[5])

# [start:stop:step]

arr_b = arr[:]
print(arr_b)

arr_b = arr[::2]
print(arr_b)

arr_b = arr[3:6]
print(arr_b)

arr_b = arr[3:]
print(arr_b)