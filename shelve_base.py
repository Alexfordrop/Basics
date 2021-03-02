import shelve

# запись данных
with shelve.open('data') as shelf:
    shelf['key'] = {'int': 7, 'float': 12.5, 'string': 'something'}

# чтение данных
with shelve.open('data') as shelf:
    print(shelf['key'])