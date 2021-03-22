print(abs(-10))

skorost = -120
if abs(skorost) > 0:
    print("Игрок движется")

if skorost > 0 or skorost < 0:
    print("Игрок движется")

s = "hi" # получение информации об объекте
dir(s)
print(dir(s))

h = "Hello" # делает символы большими
print(h)
print(h.upper())

eval('''print("Hi again 777")''') # передача команды в Python

# print("Введите выражение: ")
# v = input()
# print("Результат: ", eval(v))


# exec для вызова более сложных команд
exec('''s = 10 
b = 20
print(s + b)
''')


sp = [67, 4, 9, 30, 45, 233, 3]
print(max(sp))
print(min(sp))
print(sum(sp))
print(sum(range(0, 20, 3)))

f = open("my_file.txt", "w")
f.write("Hi my file!")
f.close()

f = open("123ty.txt")
r = f.read()
print(r)