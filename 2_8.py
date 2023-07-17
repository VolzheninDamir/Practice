n = int(input("Введите число"))
if n >= 0:
    for i in range(0, n + 2):
        if i ** 2 > n:
            print(i)
            break
        else:
            continue
