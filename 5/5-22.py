# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/fzxdW/naimien-shii-polozhitiel-nyi

# Наименьший положительный

# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент, а значения
# всех элементов списка по модулю не превосходят 1000.

data = tuple(map(int, input().split()))

min_posintive = 1000

for value in data:
    if 0 < value < min_posintive:
        min_posintive = value

print(min_posintive)
