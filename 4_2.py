def find_palindromes(line):
    palindroms = []
    n = len(line)

    # Проверяем все возможные подстроки
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = line[i:j]

            # Проверяем, является ли подстрока палиндромом
            if substring == substring[::-1]:
                palindroms.append(substring)

    return palindroms


string = input("Введите строку: ")
palindromes = find_palindromes(string)
print("Палиндромы:", palindromes)
