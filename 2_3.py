user_num = int(input("Введите число, которое хотите проверить: "))
nums_reverse = []
check_user_num = user_num
f_num = 0

while user_num > 0:
    num = user_num % 10
    nums_reverse.append(num)
    user_num = user_num // 10
nums = nums_reverse[::-1]

count = len(nums)

for number in nums:
    f_num = f_num + number**count

if f_num == check_user_num:
    print("Ваше число является числом Армстронга!")
else: print("Не является")
