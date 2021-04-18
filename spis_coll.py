# исходный список чисел
numbers = [1, 2, 3, 4, 5]

# через цикл for
squares = []
for num in numbers:
    squares.append(num * num)
    print(squares.append(num * num))

# через генератор списка
squares = [num * num for num in numbers]
print(squares)
# через функцию map
squares = map(lambda x: x * x, numbers)
print(squares)