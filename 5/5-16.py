# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/8rg1F/posliednii-maksimum

# Последний максимум

# Найдите наибольшее значение в списке и индекс последнего элемента, который
# имеет данное значение за один проход по списку, не модифицируя этот список и
# не используя дополнительного списка.

data = tuple(map(int, input().split()))

i = len(data) - 1
max_index = i
maximum = data[max_index]

while i >= 0:
    if data[i] > maximum:
        maximum = data[i]
        max_index = i
    i -= 1

print(maximum, max_index)
