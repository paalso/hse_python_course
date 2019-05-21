# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/zNzOz/maksimum-triekh-chisiel
# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).

n = int(input())
m = int(input())
q = int(input())

max = n

if m > max:
    max = m

if q > max:
    max = q

print(max)
