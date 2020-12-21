# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/P5qTq/prostyie-chisla

# Простые числа

# Выведите все простые на отрезке [2;n].

import math


def is_prime(n):
    return n == 2 or (n > 2 and all(map(lambda k: n % k, range(2, int(math.sqrt(n)) + 1))))


print(*filter(is_prime, range(2, int(input()) + 1)))

##FAIL:
##Precompile check failed:
##not functional enough