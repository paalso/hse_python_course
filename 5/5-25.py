# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/z6hIc/pieriestavit-v-obratnom-poriadkie

# Переставить в обратном порядке

# Переставьте элементы данного списка в обратном порядке, затем выведите
# элементы полученного списка. Эта задача отличается от предыдущей тем, что вам
# нужно изменить значения элементов самого списка, поменяв местами A[0] c
# A[n-1], A[1] с A[n-2], а затем вывести элементы списка подряд.
#
# Предлагается в учебных целях проделать это вручную, например, не используя
# срезов и стандартных функций.

data = list(map(int, input().split()))

last_index = len(data) - 1
for i in range(len(data) // 2):
    data[i], data[last_index - i] = data[last_index - i], data[i]

print(*data)
