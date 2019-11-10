# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/HSsxZ/pieriestavit-sosiedniie

# Переставить соседние

# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

data = list(map(int, input().split()))

for i in range(1, len(data), 2):
    data[i - 1], data[i] = data[i], data[i - 1]

print(*data)
