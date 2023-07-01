import random
win = 0
lose = 0
while lose < 3:
    user_pick = int(input("Ваш выбор: Орел - 0 или Решка - 1 "))
    random_pick = random.randint(0, 1)
    if user_pick == random_pick:
        win += 1
        lose = 0
        print("Победа")
    elif (user_pick != 1 and user_pick != 0):
        print("Конец игры")
        break
    else:
        lose += 1
        print("Поражение")
if lose == 3:
    print("Вы проиграли")
