# Дано два числа X и Y без ведущих нулей
# Необходимо проверить, можно ли получить первое из второго
# Перестановкой цифр

def isdigitpermtation(x, y):
    def countdigits(num):
        digitcount = [0] * 10
        while num > 0:
            lastdigit = num % 10
            digitcount[lastdigit] += 1
            num //= 10
        return digitcount

    digitsx = countdigits(x)
    digitsy = countdigits(y)
    for digit in range(10):
        if digitsx[digit] != digitsy[digit]:
            return False
    return True