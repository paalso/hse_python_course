# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/JhcRk/kolichiestvo-razlichnykh-eliemientov

# Количество различных элементов

# Дан список, упорядоченный по неубыванию элементов в нем.Определите,
# сколько в нем различных элементов.
data = tuple(map(int, input().split()))
counter = 1

for i in range(1, len(data)):
    if data[i] != data[i - 1]:
        counter += 1

print(counter)
