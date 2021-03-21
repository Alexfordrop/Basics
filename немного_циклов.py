
for a in range (0, 5):
    print('привет')
    print("Ура!!!")

print(list(range(10, 17)))

sp1 = [10, 40, 50, 77]
sp2 = ["must", "yes", "no"]
for i in range(0, 5):
    for j in range(0, 5):
        print(i, j)

found_coins = 20
magic_coins = 10
stolen_coins = 2
coins = found_coins

print(found_coins + 365 * (magic_coins - stolen_coins))

for i in range(0,  365):
    coins = coins + magic_coins - stolen_coins
    print("День %s Стало монет %s" % (i, coins))