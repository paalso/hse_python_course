# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/bfPaN/dvoichnyi-logharifm

# Двоичный логарифм
# По данному натуральному числу N выведите такое наименьшее целое число k, что 2ᵏ≥N.

n = int(input())

k = 0
exp_2 = 1

while exp_2 < n:
    exp_2 *= 2
    k += 1

print(k)
