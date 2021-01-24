def sayHello():
    print('Привет, всем!')

sayHello()
def printBro(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')
printBro(3, 4)
x = 5
y = 7
printBro(x, y)