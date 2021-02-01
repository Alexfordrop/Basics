ab = {  'Alex'    : 'alx@lex.com',
        'Larry'   : 'larry@dec.com',
        'Jim'     : 'jimmy@ji.com',
        'Spammer' : 'spammer@hotmail.com',
    }

print("Адрес Alex'a:", ab['Alex'])
del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])