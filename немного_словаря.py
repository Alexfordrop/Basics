d = {'a': 0, 'b': 1, 'c':0}
if d['a'] > 0:
    print('ok')
elif d['b'] > 0:
    print('ok')
elif d['c'] > 0:
    print('ok')
elif d['d'] > 0:
    print('ok')
else:
    print('not ok')

# d['d'] относится к несуществующему ключу, но код в данном elif 
# не выполняется т.к. ранее условие elif d['d'] > 0 выдаёт True
# (и остальные elif не выполняются)