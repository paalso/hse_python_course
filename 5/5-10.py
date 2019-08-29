# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/pxDtW/summa-faktorialov/submission

# Сумма факториалов

# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.

n = int(input())

f = 1
sum = 0

for k in range(1, n + 1):
    f *= k
    sum += f

print(sum)
