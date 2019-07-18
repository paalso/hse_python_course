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
