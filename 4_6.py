alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_rot13 = "nopqrstuvwxyzabcdefghijklm"
s = {a: b for a, b in zip(alphabet, alphabet_rot13)}

string = input("Введите строку: ")

new_string = ""
for letter in string:
    if letter in alphabet:
        new_string += s[letter]
    else:
        new_string += letter

print(new_string)
