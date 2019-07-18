# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/oxiW1/prinadliezhit-li-tochka-kvadratu-2/submission

# Принадлежит ли точка квадрату - 2
# Даны два действительных числа x и y. Проверьте, принадлежит ли точка с
# координатами(x,y) заштрихованному квадрату (включая его границу). Если
# точка принадлежит квадрату, выведите слово YES,иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1.


def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


def PrintAnswer(predicate, yesAnswer = "YES", noAnswer = "NO"):
    if(predicate):
        print(yesAnswer)
    else:
        print(noAnswer)


x = float(input())
y = float(input())

PrintAnswer(IsPointInSquare(x, y))
