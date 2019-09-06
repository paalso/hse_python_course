# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/b3ZNW/bol-shie-svoikh-sosiediei

# Больше своих соседей

# Дан список чисел. Определите, сколько в этом списке элементов, которые больше
# двух своих соседей и выведите количество таких элементов.

data = tuple(map(int, input().split()))

counter = 0
for i in range(1, len(data) - 1):
    if data[i - 1] < data[i] > data[i + 1]:
        counter += 1

print(counter)
