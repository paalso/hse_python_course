# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/QpJac/prinadliezhit-li-tochka-oblasti

# Принадлежит ли точка области
# Проверьте, принадлежит ли точка данной закрашенной области


def IsPointInArea(x, y):
    b1 = y >= -x and y >= 2 * x + 2
    b2 = (x + 1) ** 2 + (y - 1) ** 2 <= 4
    b3 = y <= -x and y <= 2 * x + 2
    b4 = (x + 1) ** 2 + (y - 1) ** 2 >= 4
    return (b1 and b2) or (b3 and b4)


def PrintAnswer(predicate, yesAnswer="YES", noAnswer="NO"):
    if(predicate):
        print(yesAnswer)
    else:
        print(noAnswer)


x = float(input())
y = float(input())

PrintAnswer(IsPointInArea(x, y))
