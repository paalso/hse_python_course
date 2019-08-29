# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/NY8PQ/diofantovo-uravnieniie-2/submission

# Диофантово уравнение - 2

# Даны числа a, b, c, d, e. Подсчитайте количество таких целых чисел
# от 0 до 1000 (включительно), которые являются корнями уравнения
# (ax³+bx²+cx+d)/(x-e)=0, и выведите их количество


def check_equation(a, b, c, d, e, x):
    """ Checks equality of the expression (ax³+bx²+cx+d)/(x-e) == 0 """
    return x * (x * (a * x + b) + c) + d == 0 and x != e


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

counter = 0
for x in range(0, 1001):
    if check_equation(a, b, c, d, e, x):
        counter += 1

print(counter)
