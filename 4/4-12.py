## https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/w6nuj/otritsatiel-naia-stiepien/submission

# Отрицательная степень
# Дано действительное положительное число a и целоe число n. Вычислите aⁿ.
# Решение оформите в виде функции power(a, n). Стандартной функцией возведения
# в степерь пользоваться нельзя.
# Здесь не нужна рекурсия.


def power(a, n):
    is_negative = False
    if n < 0:
        is_negative = True
        n = - n

    p = 1
    for k in range(n):
        p *= a

    if is_negative:
        return 1 / p
    return p

a = float(input())
n = int(input())

print(power(a, n))
