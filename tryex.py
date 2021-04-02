print("Введите число a")
try:
    a = float(input())
    procent = 100 / a
    print("100 / a = %s" % procent)
except  ValueError:
    print("Вы ввели не число")
except  ZeroDivisionError:
    print("Не дели на 0!!!")
except:
    print("Возникла ошибка!")
# Выполняется когда нет ошибок
else:
    print("Все выполнилось без ошибок") 
# Выполняется всегда
finally:
    print("Блок выполняется в любом случае")