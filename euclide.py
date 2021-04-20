# Необходимо найти наибольший общий делитель натуральных чисел a и b
def Euclidean_algoritm(a: int, b: int) -> int:
    while (a != 0) and (b != 0):
        if a < b:
            b %= a
        else:
            a %= b
    return a + b

test_data = {
    (10, 6) : 2,
    (24, 5) : 1,
    (27, 9) : 9,
    (105, 30) : 15,
    (240, 44) : 4
}

for pair in test_data:
    a, b = pair
    answer = Euclidean_algoritm(a, b)
print('НОД({0},{1}) - {2} : {3}'. format(pair[0],
                        pair[1],
                        answer,
                        answer == test_data[pair]))