# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/G5oDi/tip-trieughol-nika

# Тип треугольника
# Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами. 
# Выведите одно из четырех слов: rectangular для прямоугольного треугольника, 
# acute для остроугольного треугольника, obtuse для тупоугольного треугольника 
# или impossible, если треугольника с такими сторонами не существует 
# (считаем, что вырожденный треугольник тоже невозможен).



def isTriangle(x, y, z):
    return x > 0 and y > 0 and z > 0 and x < y + z and y < x + z and z < x + y


def cos(x, y, z):
    return 0.5 * (x * x + y * y - z * z) / (x * y)


def isPyth(x, y, z):
    return x * x + y * y == z * z


def isRectangularTriangle(x, y, z):
    return isPyth(x, y, z) or isPyth(x, z, y) or isPyth(y, z, x)


def isAcuteTriangle(x, y, z):
    return cos(x, y, z) > 0 and cos(x, z, y) > 0 and cos(y, z, x) > 0


def isObtuseTriangle(x, y, z):
    return not (isAcuteTriangle(x, y, z) or isRectangularTriangle(x, y, z))


x = int(input())
y = int(input())
z = int(input())

if (not isTriangle(x, y, z)):
    print('impossible')
else:
    if (isRectangularTriangle(x, y, z)):
        print('rectangular')
    elif (isAcuteTriangle(x, y, z)):
        print('acute')
    else:
        print('obtuse')
