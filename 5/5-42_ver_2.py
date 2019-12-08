# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7886R/szhatiie-spiska

# Сжатие списка

# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые
# элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

# true version

def find_non_zero(data, start):
    for i in range(start, len(data)):
        if data[i] != 0:
            return i
    return -1


data = list(map(int, input().split()))

size = len(data)
zero_index = -1
while True:
    zero_index = data.index(0, zero_index + 1)
    index = find_non_zero(data, zero_index + 1)
    if index == -1:
        break
    data[zero_index], data[index] = data[index], data[zero_index]

print(*data)
