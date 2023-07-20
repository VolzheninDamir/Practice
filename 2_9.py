import collections

number = int(input("Введите число"))
const_number = number
nums_reverse = []
while number > 0:
    num = number % 10
    nums_reverse.append(num)
    number = number // 10
nums = nums_reverse[::-1]
mx = max(nums)
index = nums.index(mx)
print(
    f'Порядковый номер максимальной цифры {mx} в числе {const_number} от начала числа = {index + 1}, а от конца = {len(nums) - index}')
