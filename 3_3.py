is_even = lambda n: n % 2 == 0

n = int(input("Введите число: "))
if is_even(n):
    print("Число", n, "является четным.")
else:
    print("Число", n, "не является четным.")