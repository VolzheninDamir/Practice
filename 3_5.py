def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Введите число до которого нужно проверить: "))
not_primes = [x for x in range(2, n+1) if not is_prime(x)]
print(not_primes)