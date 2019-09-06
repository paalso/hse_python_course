# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/tFQ4D/shieriengha

# Шеренга

# Программа получает на вход невозрастающую последовательность натуральных
# чисел,означающих рост каждого человека в строю. После этого вводится число X
# рост Пети.Все числа во входных данных натуральные и не превышают 200.
#
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть
# люди с одинаковым ростом,таким же, как у Пети, то он должен встать после них.

data = list(map(int, input().split()))
height = int(input())

if height > data[0]:
    position = 1
elif height <= data[len(data) - 1]:
    position = len(data) + 1
else:
    for index, value in enumerate(data):
        if height > value:
            position = index + 1
            break

print(position)
