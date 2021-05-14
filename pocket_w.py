#! Программа Обменный пункт
 
print("Для выхода нажмите Y")
 
while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    cache = round(money / 75, 2)
    print("К выдаче", cache, "долларов")
 
print("Работа обменного пункта завершена")