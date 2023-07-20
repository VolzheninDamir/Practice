string = input("Введите строку: ")
charcountdict = {char: string.count(char) for char in set(string) if char != " "}
print(charcountdict)
