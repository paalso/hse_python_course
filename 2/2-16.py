# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/5zNLl/chietnyie-i-niechietnyie

# Четные и нечетные
# Даны три целых числа A, B, C. Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.

def isSameParity(x, y):
    return (x - y) % 2 == 0


x = int(input())
y = int(input())
z = int(input())

if isSameParity(x, y) and isSameParity(x, z) and isSameParity(y, z):
    print('NO')
else:
    print('YES')
