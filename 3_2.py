fibonacci = lambda n: [0, 1] if n == 1 else fibonacci(n - 1) + [
    fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]] if n > 1 else []

n = int(input("Введите число: "))
fibonacci_numbers = fibonacci(n)
print("Список чисел Фибоначчи до", n, ":", fibonacci_numbers)
