# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/0OyhQ/iskliuchaiushchieie-ili/submission

# Исключающее ИЛИ

# Напишите функцию xor(x, y) реализующую функцию "Исключающее ИЛИ" двух
# логических переменных x и y.
# Функция xor должна возвращать True, если ровно один из ее аргументов x или y,
# но не оба одновременно равны True.


def xor(x, y):
    return int((x and not y) or (not x and y))


x = int(input())
y = int(input())

print(xor(x, y))
