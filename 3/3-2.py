# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/Cm2bR/summa-riada/submission

# Сумма ряда
# По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).

n = int(input())

sum = 0.0
for k in range(1, n + 1):
    sum += 1 / (k * k)

print(sum)
