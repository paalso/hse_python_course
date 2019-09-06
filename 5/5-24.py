# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/f2UfT/vyviesti-v-obratnom-poriadkie

# Вывести в обратном порядке

# Выведите элементы данного списка в обратном порядке, не изменяя сам список

data = tuple(map(int, input().split()))

print(*data[::-1])
