# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/CSkuE/koordinatnyie-chietvierti

# Координатные четверти
# Даны координаты двух точек на плоскости, требуется определить, 
# лежат ли они в одной координатной четверти или нет (все координаты отличны от нуля).

def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if sgn(x1) == sgn(x2) and sgn(y1) == sgn(y2):
    print('YES')
else:
    print('NO')
