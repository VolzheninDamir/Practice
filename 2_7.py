sum = 0
flag = False
while flag == False:
    user_num = int(input("Введите отрицательное число"))
    if user_num < 0:
        sum += user_num
    else:
        flag = True
print(sum)