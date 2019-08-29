# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/r6MQp/riad-1

# Ряд - 1
# Даны два целых числа A и B (при этом A≤B). Выведите все числа от A до B включительно.

a, b = int(input()), int(input())
print(*[n for n in range(a, b + 1)])
