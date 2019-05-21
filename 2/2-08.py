# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/07rub/tsviet-klietok-shakhmatnoi-doski

# Цвет клеток шахматной доски
# Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, 
# а если в разные цвета – то NO.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 + y1 - x2 - y2) % 2 == 0
    print('YES')
else:
    print('NO')
