# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/py6mg/sortirovka

# Сортировка

# Отсортируйте данный массив, используя встроенную сортировку.

input()
data = list(map(int, input().split()))
data.sort()
print(*data)
