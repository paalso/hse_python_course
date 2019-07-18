# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/GYhFu/prinadliezhit-li-tochka-kvadratu-1/submission

# Принадлежит ли точка квадрату - 1
# Даны два действительных числа x и y. Проверьте, принадлежит ли точка с
# координатами (x,y) заштрихованному квадрату (включая его границу). Если
# точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1.

def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1


def PrintAnswer(predicate):
    if(predicate):
        print("YES")
    else:
        print("NO")


x = float(input())
y = float(input())

PrintAnswer(IsPointInSquare(x, y))
