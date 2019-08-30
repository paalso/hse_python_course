# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/TlM9p/kolichiestvo-polozhitiel-nykh

# Количество положительных

# Найдите количество положительных элементов в данном списке.

l = list(map(int, input().split()))
print(len(tuple(n for n in l if n > 0)))
