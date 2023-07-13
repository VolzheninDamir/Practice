from itertools import permutations

arr = input("Введите элементы списка через пробел: ").split()
arr = [int(num) for num in arr]

print("Исходный список:", arr)
print("Варианты списка:")
perm = permutations(arr)
count = 0
for i in perm:
    print(i)
    count += 1

print("Количество перестановок:", count)
