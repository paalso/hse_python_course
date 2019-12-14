# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ML248/proizviedieniie-piatykh-stiepieniei

# Произведение пятых степеней

# На вход подаётся последовательность натуральных чисел длины n≤1000.Посчитайте
# произведение пятых степеней чисел в последовательности.

from functools import reduce

print(
    reduce(
        lambda x, y: x * y, map(
            lambda x: x ** 5,
            map(int,open('input.txt', 'r').read().split()
            )
        )
    )
)
