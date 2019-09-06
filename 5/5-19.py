# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/oHcKg/vozrastaiet-li-spisok

# Возрастает ли список?

# Дан список чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа. Если соседних элементов одного знака нет - не выводите
# ничего. Если таких пар соседей несколько - выведите первую пару.


def sgn(number):
    if number > 0:
        return +1
    if number < 0:
        return -1
    return 0


def is_same_sgn(num1, num2):
    return sgn(num1) == sgn(num2)


data = tuple(map(int, input().split()))

for i in range(1, len(data)):
    if is_same_sgn(data[i - 1], data[i]):
        print(data[i - 1], data[i])
        break
