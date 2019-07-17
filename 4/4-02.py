# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/jDGCr/dlina-otriezka/submission

# Длина отрезка
# Даны четыре действительных числа: x₁, y₁, x₂, y₂. Напишите функцию
# distance(x1, y1, x2, y2), вычисляющую расстояние между точками (x₁,y₁) и
# (x₂,y₂). Считайте четыре действительных числа и выведите результат работы
# этой функции.


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))
