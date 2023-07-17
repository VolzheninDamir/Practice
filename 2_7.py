sum = 0
flag = False
while not flag:
    user_num = int(input("Введите отрицательное число"))
    if user_num < 0:
        sum += user_num
    else:
        flag = True
print(sum)
