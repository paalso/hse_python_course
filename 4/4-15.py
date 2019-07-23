# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/HBMwd/alghoritm-ievklida/submission

# Алгоритм Евклида
# Для быстрого вычисления наибольшего общего делителя двух чисел используют
# алгоритм Евклида. Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b)
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).


def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)


n = int(input())
m = int(input())

print(gcd(n, m))
