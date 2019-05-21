# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/MLmFh/kakoie-chislo-bol-shie

# Какое число больше?
# Даны два целых числа. Программа должна вывести число "1", если первое число больше второго, 
# число "2", если второе больше первого или число "0", если они равны.

n = int(input())
m = int(input())

if n > m:
    print(1)
elif n < m:
    print(2)
else:
    print(0)
