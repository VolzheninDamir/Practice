def printShow(tv):
    for show in tv:
        print(show)

tv = ["Универ","Импровизация", "Однажды в России", "Студия Союз"]

printShow(tv)

user_show = str(input("Введите название передачи - "))
num_show = int(input("Введите желаемую позицию передачи в списке - "))

tv.insert(num_show - 1, user_show)
printShow(tv)