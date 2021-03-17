print('Введите ваш возраст')
age = int(input())

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
