# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/nNfBN/sistiema-linieinykh-uravnienii-1/submission

# Система линейных уравнений - 1

# Даны вещественные числа a, b, c, d, e, f. Известно, что система линейных
# уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой
# системы.


def discriminant(a, b, c, d):
    return a * d - b * c


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = discriminant(e, b, f, d) / discriminant(a, b, c, d)
y = discriminant(a, e, c, f) / discriminant(a, b, c, d)

print(x, y)
