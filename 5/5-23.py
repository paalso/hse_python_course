# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/a8kYY/naimien-shii-niechietnyi

# Наименьший нечетный

# Выведите значение наименьшего нечетного элемента списка, гарантируется,
# что хотя бы один нечётный элемент в списке есть.

data = tuple(map(int, input().split()))

min_odd = None

for index, item in enumerate(data):
    if item % 2 == 1:
        min_odd = item
        break


for _, item in enumerate(data, start=index):
    if item % 2 == 1 and item < min_odd:
        min_odd = item

print(min_odd)
