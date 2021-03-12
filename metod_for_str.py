str1 = 'Привет, как у тебя дела?'
str1.find('?')
print(str1.find('?'))
print(str1.find('и'))
print(str1. rfind('т'))
print(str1.find('т,,')) # ничего не нашлось, поэтому выводит -1

# отличие find от index
print(str1.find('как'))
print(str1.find('т'))
print(str1. rfind('т'))
print(str1.find('т,,'))

print(str1.index('как'))
print(str1.index('т'))
print(str1. rindex('т'))
# print(str1.rindex('т,,'))  # выводит ошибку


#
print(str1.replace('дела', 'настроение'))

print(str1.replace(' ', ''))

# разбивка на список split
str1_array = str1.split(' ')
print(str1_array)

str2 = '01.jpg#02.jpg#tryyr#jpg.jpg#567.jpg'
str2_array = str2.split('#')
print(str2_array)