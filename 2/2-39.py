# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/tu0QY/kolichiestvo-eliemientov-bol-shie-priedydushchiegho

# Количество элементов, больше предыдущего
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

counter = 0
n = int(input())

while n != 0:
    prev = n
    n = int(input())
    if n > prev:
        counter += 1

print(counter)

