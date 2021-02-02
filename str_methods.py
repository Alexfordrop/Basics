name = 'Alexey'

if name.startswith('Ale'):
    print('Да, строка начинается на "Ale"')

if 'A' in name:
    print('Да, она содержит строку "a"')

if name.find('lex') != -1:
    print('Да, она содержит строку "Lex"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))