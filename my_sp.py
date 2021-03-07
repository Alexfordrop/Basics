# СПИСКИ
sp1 = ['яблоки', 'бананы', 'виноград', 'грибы', 'картошка']
print(sp1)

print(sp1[0])

sp1[3] = 'морковь'
print(sp1)

# добавляем новый элемент
sp1.append("сыр")
print(sp1)

# удаляем элемент
del sp1[1]
print(sp1)

#
sp2 = [234, 4235, 640, 345, 67]
sp3 = [24566, 'dfg', 2345555, 'nb', 6555]
sp4 = [sp2, sp3, sp1]
print(sp4)
print(sp4[1] [3])

sp5 = [1, 2, 3]
sp6 = [4, 5, 6]
sp7 = sp5 + sp6
print(sp7)

sp8 = [5,7]
sp9 = sp8 *6
print(sp9)

print(sp1[2:])
print(sp1[1 : 3])