# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7886R/szhatiie-spiska

# Сжатие списка

# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые
# элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

data = list(map(int, input().split()))

i = 0
j = len(data) - 1
while True:
    while data[i] != 0:
        i += 1
    while data[j] == 0:
        j -= 1
    if i >= j:
        break
    data[i] = data[j]
    data[j] = 0

print(*data)
