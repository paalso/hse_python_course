# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/3mr1b/tsiklichieskii-sdvigh-vpravo

# Циклический сдвиг вправо

# Циклически сдвиньте элементы списка вправо(A[0] переходит на место A[1],
# A[1] на место A[2], ..., последний элемент переходит на место A[0]).

data = list(map(int, input().split()))

last = data[len(data) - 1]
for i in range(len(data) - 1, 0, -1):
    data[i] = data[i - 1]
data[0] = last

print(*data)
