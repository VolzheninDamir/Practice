def binary_dict():
    binary_dict = {}
    for num in range(1, 11):
        binary_dict[num] = bin(num)[2:]
    return binary_dict


print(binary_dict())
