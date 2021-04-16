# fact(5) = 1*2*3*4*5
def fact(num):
    if num == 0:
        #print(1)
        return 1
    else:
        print(num)
        return num * fact(num - 1)

print('Факториал: %s' % fact(5))