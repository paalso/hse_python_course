# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/tP4zg/slozhieniie-biez-slozhieniia/submission

# Сложение без сложения
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только
# +1 и -1. Также нельзя использовать циклы.


def sum(a, b):
    if b == 0:
        return a
    if b < 0:
        return sum(a, b + 1) - 1
    return sum(a, b - 1) + 1


a = int(input())
b = int(input())

print(sum(a, b))
