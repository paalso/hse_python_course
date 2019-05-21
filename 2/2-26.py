# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/wH3BE/spisok-kvadratov/submission

# Список квадратов
# По данному целому числу N распечатайте все квадраты натуральных чисел,не превосходящие N, в порядке возрастания.

n = int(input())

k = 1
sqr = k * k
while (sqr <= n):
    print(sqr, end=' ')
    k += 1
    sqr = k * k
