# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/M4YL4/prinadliezhit-li-tochka-krughu/submission

# Принадлежит ли точка кругу
# Даны пять действительных чисел: x, y, xc, yc, r.
# Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.
# Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


def PrintAnswer(predicate, yesAnswer="YES", noAnswer="NO"):
    if(predicate):
        print(yesAnswer)
    else:
        print(noAnswer)


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

PrintAnswer(IsPointInCircle(x, y, xc, yc, r))
