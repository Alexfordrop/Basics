# ...10.....50....60....100...
a = 50
b = 100

a1 = 10
b1 = 60

print('Введите число d: ')
d = int(input())
if d > a and d < b:
    print('d > 50 and d < 100')

if d > a1 and d < b1 and d > a and d < b:
    print('d находится в 2 интервалах')

if d > 200 or d >300:
    print('d > 200 или d > 300')

if not d > 500:
    print('not  d <= 500')