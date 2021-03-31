## any all
sp1 = [True, False, True]
if all(sp1):
    print("Все элементы True")
else:
    print("Не все элементы True")

if any(sp1):
    print("Хотя бы 1 элемент True")

if any(sp1) or not all(sp1):
    print("Есть элемент True и False")

sp2 = [1, 15, 50, 100, 200]
if any(number > 50 for number in sp2):
    print("Есть число больше 50")

if all(number > 0 for number in sp2):
    print("Все числа больше нуля")