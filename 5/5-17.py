# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ASlVF/bol-shie-priedydushchiegho/submission

# Больше предыдущего

# Дан список чисел. Выведите все элементы списка,
# которые больше предыдущего элемента.

data = tuple(map(int, input().split()))

i = len(data) - 1
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        print(data[i], end=' ')
