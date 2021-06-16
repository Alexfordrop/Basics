# Левый и правй бинарный поиск
def lbinsearch(l, r, check, checkparams):   # левый
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def rbinsearch(l, r, check, checkparams):    # правый
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            l = m - 1
    return l