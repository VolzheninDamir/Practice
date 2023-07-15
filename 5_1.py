import csv

# Список книг
caption = ["Книга", "Автор", "Год выпуска"]
books = [["Преступление и наказание", "Федор Достоевский", "1866"],
         ["Горе от ума", "Александр Грибоедов", "1831"],
         ["Отцы и дети", "Иван Тургенев", "1862"],
         ["Обломов", "Иван Гончаров", "1859"],
         ["Мертвые души", "Николай Гоголь", "1842"]]

filename = "books.csv"

with open(filename, "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(caption)
    writer.writerows(books)
