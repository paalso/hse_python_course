# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/4zxQo/slozhnoie-uravnieniie

# Сложное уравнение
# Решить в целых числах уравнение: (ax+b) / (cx+d) =0

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0 and (c != 0 or b != 0):
    print("INF")
elif a * d == b * c or a == 0 and b != 0 or b % a != 0:
    print("NO")
else:
    print(- b // a)
