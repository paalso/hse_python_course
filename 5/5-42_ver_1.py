# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7886R/szhatiie-spiska

# Сжатие списка

# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые
# элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

data = list(map(int, input().split()))

zeros = 0
for el in data:
    if el != 0:
        print(el, end=' ')
    else:
        zeros += 1

print('0 ' * zeros)
