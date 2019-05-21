# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/kmSNa/znak-chisla

# Знак числа
# Для данного числа x выведите значение sign(x).

x = int(input())

sgn = 0

if x > 0:
    sgn = 1
elif x < 0:
    sgn = -1
else:
    sgn = 0

print(sgn)
