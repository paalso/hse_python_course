from math import sqrt


def squares_sum(l):
    sum = 0
    for el in l:
        sum += el * el
    return sum


def lagrange(n):
    result = []
    sqrt_n = int(sqrt(n))
    if sqrt_n **2 == n:
        result.append(sqrt_n)
        return result

    for i in range(1, sqrt_n + 1):
        tmp = squares_sum(lagrange(n - i * i))
        if tmp and i * i + squares_sum(lagrange(n - i * i)) == n:
            result.append(i)
            return result


n = int(input())
print(*lagrange(n))

