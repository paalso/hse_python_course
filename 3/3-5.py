# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/HO43Q/okrughlieniie-po-rossiiskim-pravilam

# Округление по российским правилам
# По российский правилам числа округляются до ближайшего целого числа,
# а если дробная часть числа равна 0.5, то число округляется вверх.
# Дано неотрицательное число x, округлите его по этим правилам.
# Обратите внимание, что функция round не годится для этой задачи!

def russian_round(x):
    int_x = int(x)
    if x - int_x == int_x + 1 - x:
        return int_x + 1
    return round(x)


x = float(input())

print(russian_round(x))
