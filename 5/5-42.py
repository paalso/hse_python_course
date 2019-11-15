# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7886R/szhatiie-spiska

# Сжатие списка

# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые
# элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

# 90% - Test 10: Time Limit Exceeded

data = list(map(int, input().split()))

size = len(data)
zeros = 0
k = 0
while k < size:
    if data[k] != 0:
        k += 1
    else:
        flag = True
        for i in range(k + 1, size - zeros):
            data[i - 1] = data[i]
            if data[i] != 0:
                flag = False
        if flag:
            break
        data[size - 1 - zeros] = 0
        zeros += 1

print(*data)
