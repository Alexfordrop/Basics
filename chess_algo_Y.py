# На шахматной доске N * N находятся M ладей(ладья бьет по горизонтали и вертикали)
# Сколько пар ладей бьютдруг друга
# Ладьи задаются парой чисел I, J обозначающие координаты клетки

def countbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs
    
    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) + countpairs(rooksincol)