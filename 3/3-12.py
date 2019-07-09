##https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/tjYS5/sistiema-linieinykh-uravnienii-2/submission

# Система линейных уравнений - 2

# Даны числа a, b, c, d, e, f. Решите систему линейных уравнений
# ax + by = e
# cx + dy = f


def discriminant(a, b, c, d):
    return a * d - b * c


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

discr = discriminant(a, b, c, d)

if discr != 0:
    x = discriminant(e, b, f, d) / discriminant(a, b, c, d)
    y = discriminant(a, e, c, f) / discriminant(a, b, c, d)
    print(2, x, y)
elif b != 0 and a != 0 and c * e == a * f:
    print(1, - a / b, e / b)
elif b == 0 and a != 0 and c * e == a * f:
    print(3, e / a)
elif a == 0 and b != 0 and d * e == b * f:
    print(4, e / b)

elif d != 0 and c != 0 and c * e == a * f:
    print(1, - c / d, f / d)
elif d == 0 and c != 0 and c * e == a * f:
    print(3, f / c)
elif c == 0 and d != 0 and d * e == b * f:
    print(4, f / d)

elif a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
else:
    print(0)
