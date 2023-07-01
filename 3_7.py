def vowel_dict(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_dict = {}
    for letter in string:
        if letter.lower() in vowels:
            vowel_dict[letter] = True
        else:
            vowel_dict[letter] = False
    return vowel_dict

string = input("Введите строку: ")
print(vowel_dict(string))