# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/jdzpp/ploshchad-trieughol-nika/submission

# Площадь треугольника
# Даны длины сторон треугольника. Вычислите площадь треугольника.

def square_triangle(a, b, c):
    p = 0.5 * (a + b + c)
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

a = float(input())
b = float(input())
c = float(input())

print(square_triangle(a, b, c))
