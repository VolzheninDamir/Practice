a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

sum = 0

for i in range(a, b+1):
    sum += i

print(f"Сумма всех целых чисел от {a} до {b} равна {sum}")