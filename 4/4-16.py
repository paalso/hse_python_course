# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/q1gm9/sokratitie-drob/submission

# Сократите дробь
# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m), получающая значения
# n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).


def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)


def ReduceFraction(n, m):
    k = gcd(n, m)
    return n // k, m // k


n = int(input())
m = int(input())

print(*ReduceFraction(n, m))    # * - печатает без скобок
