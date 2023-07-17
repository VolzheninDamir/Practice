a = int(input("Введите коэффициент при старшей степени(a) = "))
b = int(input("Введите коэффициент при младшей степени(b) = "))
c = int(input("Введите коэффициент при свободном члене(c) = "))

x1 = 0
x2 = 0
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("Нет решений")
elif discriminant == 0:
    x1 = (-1 * b + discriminant**0.5)/(2*a)
    print(f'Существует только одно решение, где х = {x1}')
else:
    x1 = (-1 * b + discriminant**0.5)/(2*a)
    x2 = (-1 * b - discriminant**0.5)/(2*a)
    print(f'Существует два решения, где х1 = {x1} , а х2 = {x2}')
