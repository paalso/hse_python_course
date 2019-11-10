# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/nh0SC/unikal-nyie-eliemienty

# Уникальные элементы

# Дан список. Выведите те его элементы, которые встречаются в списке только
# один раз. Элементы нужно выводить в том порядке, в котором они встречаются
# в списке.

data = list(map(int, input().split()))

size = len(data)
flag = True

for i, el in enumerate(data):
    for j in range(size):
        if i == j:
            continue
        if data[j] == el:
            flag = False
            break
    if flag:
        print(el, end=" ")
    flag = True
