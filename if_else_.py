f = '10'
if f == str(10):
    print('f == 10')

h = 10
if h == int('10'):
    print('h == 10')

j = '2.53'
print(float(j) + 7.5)
if float(j) + 7.5 > 10:
    print('Это больше 10')


print('Введите ваш возраст')
age = int(input())

if age == 5:
    print('5')
elif age == 6:
    print('6')
elif age == 7:
    print('7')

if age < 100:
    print('Возраст меньше 100')
else:
    print('Вам больше 100')

if age > 20:
    print('О, вы уже взрослый!')
    print('Вам 20!!!')

if age < 20:
    print('Об вы ещё маленький!')

if age == 18:
    print('Ура, мне 18!')

if age >= 30 and age <=40:
    print('О, от 30 до 40!')

if age == 50 or age == 60 or age == 70 or age ==80:
    print('О, у вас юбилей!')

print('Мы проверили ваш возраст!')
