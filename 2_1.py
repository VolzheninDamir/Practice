import random

colors = ["purple", "red", "yellow", "black", "orange"]

for color in colors:
    print(color)

flag = False

random_item = random.randint(0,4)
random_color = colors[random_item]

while flag == False:
    user_color = str(input("Угадайте цвет(выберите из предложенных)"))
    if user_color == random_color:
        flag = True
        print("Отлично!")
        break
    elif random_color == "red":
        print("Попробуй еще раз, подсказка: Какого цвета арбуз?")
    elif random_color == "purple":
        print("Попробуй еще раз, подсказка: Какой последний цвет радуги?")
    elif random_color == "yellow":
        print("Попробуй еще раз, подсказка: Какого цвета солнце?")
    elif random_color == "black":
        print("Попробуй еще раз, подсказка: Какого цвета уголь?")
    elif random_color == "orange":
        print("Попробуй еще раз, подсказка: Какого цвета мандарин?")
    else:
        print("Попробуй еще раз")
