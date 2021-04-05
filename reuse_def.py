p = 100
def pab():
    r = 10
    h = 20
    print(p, r, h)
pab()

def ploshad_axb(a, b):
    return a * b

def podschet_i_ves(monety, ves, nomer):
    print("Подсчёт №%s" % nomer)
    print("Всего вес монет: %s" % (monety * ves))

# print("Подсчёт №1")
podschet_i_ves(100, 2.5, 1)
# print("Подсчёт №2")
podschet_i_ves(200, 5, 2)

a1 = 100
b1 = 20
print("Площадь прямоугольника %s на %s равна %s" 
% (a1, b1, ploshad_axb(a1, b1)))

for i in range(0, 1):
    print("Введите a: ")
    a = int(input())
    print("Введите b: ")
    b = int(input())
    print("Площадь прямоугольника %s на %s равна %s" 
% (a, b, ploshad_axb(a, b)))