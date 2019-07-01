## https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/emyMl/kolichiestvo-eliemientov-ravnykh-maksimumu

## Количество элементов, равных максимуму
## Последовательность состоит из натуральных чисел и завершается числом 0.
## Определите количество элементов этой последовательности, которые равны ее
## наибольшему элементу.

n = int(input())
max = n
counter = 1

while n != 0:
    n = int(input())
    if n > max:
        max = n
        counter = 1
    elif n == max:
        counter += 1

print(counter)
