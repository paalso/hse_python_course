# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/2DGxu/summa-kvadratov/submission

# Сумма квадратов
# По данному натуральном n вычислите сумму 1²+2²+3²+...+n²

n = int(input())
sum = 0
for k in range(n + 1):
    sum += k * k
print(sum)
