import csv


def csv_add_row(filename, row):
    with open(filename, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


filename = "books.csv"

n_rows = int(input("Сколько записей вы хотите добавить?: "))
for i in range(n_rows):
    print(f"Добавление записи {i + 1}")
    book = input("Название: ")
    author = input("Автор: ")
    year = input("Год: ")
    row = [book, author, year]
    csv_add_row(filename, row)
    print("Запись добавлена.\n")

name = input("По какому автору хотите искать?: ")
with open(filename, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    found = False
    for row in reader:
        if name in row["Автор"]:
            found = True
            print("Книги этого автора: ")
            print(row["Автор"], row["Книга"], sep=", ")
    if not found:
        print("В списке нет книг этого автора!")
