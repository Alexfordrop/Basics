# find
str1 = "Hello World! This is me again!"
index = str1.find('This')
print(index)
index = str1.find('again')
print(index)

index = str1.find('o', 6)
print(index)

index = str1.find('m', str1.find('This'), str1.find('again'))
print(index)

# starswith
yesno = str1.startswith('Hello')
print(yesno)

print(str1.find('Hello') == 0) # тоже самое, но через find

# endswith
yesno = str1.endswith('again!')
print(yesno)

print(str1.find('again!') == len(str1) - len('again!')) #тоже самое, но через find