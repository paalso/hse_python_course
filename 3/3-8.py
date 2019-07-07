# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/sUqMC/standartnoie-otklonieniie

# Стандартное отклонение
# Дана последовательность натуральных чисел x₁, x₂ ..., xn.
# Стандартным отклонением называется величина
# σ=sqrt(((x₁-s)²+(x₂-s)²+…+(xn-s)²) / (n-1))
# где s = ((x₁+x₂+…+xn) / n) — среднее арифметическое последовательности,
# а sqrt - квадратный корень. Определите стандартное отклонение для данной
# последовательности натуральных чисел, завершающейся числом 0.

n = 0
sum_sqr = 0
sum = 0

while True:
    x = float(input())
    if x == 0:
        break
    sum += x
    sum_sqr += x * x
    n += 1

Av = sum / n
D = ((sum_sqr - 2 * Av * sum + n * Av * Av) / (n - 1)) ** 0.5
print(D)
