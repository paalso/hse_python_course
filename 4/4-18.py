# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/QEiwQ/chislo-sochietanii

# Число сочетаний
# По данным целым числам n и k (0≤k≤n) вычислите C из n по k.
# Решение оформите в виде функции C(n, k).
# Для решения используйте рекуррентное соотношение:
# С(n, k) = С(n - 1, k) + С(n - 1, k - 1)
# И равенства:
# С(n, 1) = n, C(n, n) = 1


def C(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1 or k == n - 1:
        return n

    return C(n - 1, k) + C(n - 1, k - 1)


n = int(input())
k = int(input())
print(C(n, k))
