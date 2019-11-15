# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7886R/szhatiie-spiska

# Сжатие списка

# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые
# элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

data = list(map(int, input().split()))

size = len(data)
zeros = 0
for i in range(size):
    if data[i] == 0:
        zeros += 1
        for j in range(i, size - zeros):
            data[j] = data[j + 1]
            data[size - zeros] = 0
        print(*data)
    if i == size - zeros - 1:
        break


print("-----")
print(*data)
