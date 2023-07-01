n = int(input("Введите число до которого нужно вывести квадраты: "))
squares = [x * x for x in range(1, n+1)]
print(squares)