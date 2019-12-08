# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/MJXOK/pieriesiechieniie-mnozhiestv

# Пересечение множеств

# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список,
# в порядке возрастания.

print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))
