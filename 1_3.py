nums = []

one = int(input("Введите первое число: "))
nums.append(one)
two = int(input("Введите второе число: "))
nums.append(two)
three = int(input("Введите третье число: "))
nums.append(three)

if (one > two) and (one > three):
    print("Наибольшее число: ", one)
elif (two > one) and (two > three):
    print("Наибольшее число: ", two)
elif one == two == three:
    print("Наибольшего нет, числа равны")
else:
    print("Наибольшее число: ", three)
r_nums = list(reversed(sorted(nums)))
print(r_nums)
