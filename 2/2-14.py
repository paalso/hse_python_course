# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/oeZuN/shashki

# На доске стоит белая шашка. Требуется определить, может ли она попасть в заданную клетку, 
# делая ходы по правилам и не пользуясь ходами дамки (т. е. не используя возможность перемещаться 
#     назад после превращения в дамку). Белые шашки могут ходить по клеткам одного цвета 
# по диагонали вверх-влево или вверх-вправо. Ходов может быть несколько!

def isSameParity(x, y):
    return (x - y) % 2 == 0


def isSameColour(x1, x2, y1, y2):
    return isSameParity(x1 + y1, x2 + y2)


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if isSameColour(x1, x2, y1, y2) and y1 < y2 and abs(x1 - x2) <= abs(y1 - y2):
    print('YES')
else:
    print('NO')
