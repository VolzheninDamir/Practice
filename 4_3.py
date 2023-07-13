def find_primes(start, end):
    primes = []

    # Проверяем все числа в диапазоне
    for num in range(start, end + 1):
        if num > 1:
            # Проверяем, является ли число простым
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    return primes


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

primes = find_primes(start, end)
print("Простые числа:", primes)
