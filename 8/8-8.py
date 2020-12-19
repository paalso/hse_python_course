# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/KF4aU/faktorialy

# Факториалы

# По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов:
# 0!,1!,2!,…,n!

from itertools import accumulate

print(*accumulate([1] + list(range(1, int(input()) + 1)), lambda x, y: x * y))
