a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
for i in a:
    if i == 0:
        [i + 1] + [-1]
    elif i == -1:
        [-2] + [0]
    else:
        [i-1] + [i+1] % len(a)
print(*a)