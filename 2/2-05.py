# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ZMk8I/khod-korolia

# Ход короля

# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. 
# Даны две различные клетки шахматной доски, определите, может ли король попасть 
# с первой клетки на вторую одним ходом.


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1 != x2 or y1 != y2):
    print('YES')
else:
    print('NO')
