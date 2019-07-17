# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/VyGOg/pierimietr-trieughol-nika/submission

# Периметр треугольника
# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр треугольника
# по координатам трех его вершин.


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def perimeter(x1, y1, x2, y2, x3, y3):
    return distance(x1, y1, x2, y2)\
            + distance(x1, y1, x3, y3)\
            + distance(x2, y2, x3, y3)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


print("{0:.6f}".format(perimeter(x1, y1, x2, y2, x3, y3)))
