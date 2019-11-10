# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/Ju34T/pieriestavit-min-i-max

# Переставить min и max

# В списке все элементы попарно различны. Поменяйте местами минимальный и
# максимальный элемент этого списка.

data = list(map(int, input().split()))

min_index = 0
max_index = 0

for index, value in enumerate(data):
    if value > data[max_index]:
        max_index = index
    if value < data[min_index]:
        min_index = index

data[min_index], data[max_index] = data[max_index], data[min_index]

print(*data)
