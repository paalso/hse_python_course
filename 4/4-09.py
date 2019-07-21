# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/WFITX/minimal-nyi-dielitiel-chisla/submission

# Минимальный делитель числа
# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n). Алгоритм должен иметь
# сложность порядка корня квадратного из n.


def MinDivisor(n):
    if n & 1 == 0:
        return 2
    upper_lim = int(n ** 0.5)
    k = 3
    while k <= upper_lim:
        if n % k == 0:
            return k
        k += 2
    return n


n = int(input())
print(MinDivisor(n))
