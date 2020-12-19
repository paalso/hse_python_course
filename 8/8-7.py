# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/WprE4/chastichnyie-summy

# Частичные суммы

# По заданной последовательности (a₁,…,an)
# посчитайте последовательность частичных сумм:
# (S₁,…,Sn), где Sk=a₁+a₂+…+ak.

from itertools import accumulate

# sequence = list(map(int, input().split()))
print(*accumulate(list(map(int, input().split())), lambda x, y: x + y))
