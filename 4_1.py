def max_permutation(a):
    num_str = str(a)
    digits = sorted(num_str, reverse=True)
    max_num = int(''.join(digits))
    return max_num


num = int(input("Введите число: "))
print("Наибольшее число: ", max_permutation(num))
