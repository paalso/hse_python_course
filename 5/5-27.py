# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/S01BF/vstavit-eliemient

# Вставить элемент

# Дан список целых чисел, число k и значение C. Необходимо вставить в список
# на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие
# индекс не менее k, вправо.
#
# Поскольку при этом количество элементов в списке увеличивается, после
# считывания списка в его конец нужно будет добавить новый элемент, используя
# метод append.
#
# Вставку необходимо осуществлять уже в считанном списке, не делая этого при
# выводе и не создавая дополнительного списка.

data = list(map(int, input().split()))
k, c = tuple(map(int, input().split()))

last_index = len(data) - 1

if k == last_index + 1:
    data.append(c)
else:
    last_element = data[last_index]
    for i in range(last_index, k, -1):
        data[i] = data[i - 1]
    data[k] = c
    data.append(last_element)

print(*data)
