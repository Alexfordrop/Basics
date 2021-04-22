a = int(input())
b = int(input())
cake = a
while cake % b != 0:
    cake += a
print(cake)