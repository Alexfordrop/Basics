s = input()
b = ''
s = s + '1'
c = s[0]
r = 0
for i in s:
    if c != i:
        b += c + str(r)
        c = i
        r = 0
    r += 1
print(b)