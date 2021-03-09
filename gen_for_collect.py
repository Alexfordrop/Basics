# Генераторный список
a = [i for i in range(5)]

# Генераторное выражение
x = (i for i in range(5))

print(a)

print(x)

for i in x:
    print(i, end=' ')
