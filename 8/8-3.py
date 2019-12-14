# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/EMsJG/naimien-shii-niechietnyi

# Наименьший нечетный

# Выведите значение наименьшего нечетного элемента списка, гарантируется,
# что хотя бы один нечётный элемент в списке есть.

print(min(filter(lambda n: n % 2 == 1, list(map(int, input().split())))))
