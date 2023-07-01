points = int(input("Введите количество очков: "))

if points == 3:
    print("Выигрыш")
elif points == 0:
    print("Проигрыш")
elif points == 1:
    print("Ничья")
else:
    print("Некорректное количество очков")
