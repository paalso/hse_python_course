# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/r6MQp/riad-1

# Ряд - 2
# Даны два целых числа A и В. Выведите все числа от A до B включительно, 
# в порядке возрастания,если A < B, или в порядке убывания в противном случае.

a, b = int(input()), int(input())
if a < b:
    print(*[n for n in range(a, b + 1)])
else:
    print(*[n for n in range(a, b - 1, -1)])
