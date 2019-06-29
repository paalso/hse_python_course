# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/keszi/summa-kvadratov

# Сумма последовательности
# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².


n = int(input())
sum = 0

for k in range(1, n + 1):
    sum += k * k

print(sum)
