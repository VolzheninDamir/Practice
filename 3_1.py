nums = input("Введите список чисел, разделенных пробелами: ").split()
nums = [int(num) for num in nums]

average = lambda nums: sum(nums) / len(nums)

print("Среднее значение списка чисел:", average(nums))