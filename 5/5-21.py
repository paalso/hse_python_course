# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/b3ZNW/bol-shie-svoikh-sosiediei

# Наибольший элемент

# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем
# индекс этого элемента в списке. Если наибольших элементов несколько,
# выведите их значение и индекс первого из них.

data = tuple(map(int, input().split()))

max_index, max_value = 0, data[0]

for index, value in enumerate(data):
    if value > max_value:
        max_index, max_value = index, value

print(max_value, max_index)
