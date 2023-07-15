import csv

with open("books.csv", encoding='utf-8') as books:
    file_reader = csv.DictReader(books, delimiter=",")
    first = input("Введите начальный год: ")
    last = input("Введите конечный год: ")
    found = False
    for row in file_reader:
        try:
            year = int(row["Год выпуска"])
            if int(first) <= year <= int(last):
                found = True
                print(row["Книга"], row["Год выпуска"], sep=", ")
        except ValueError:
            continue
    if not found:
        print("В списке нет книг в интервале этих дат!")
