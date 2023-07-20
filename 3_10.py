string = input("Введите строку: ")
charcountdict = {char: string.count(char) for char in string if char != " "}
print(charcountdict)
