# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/yGoeF/riad-3/

# Ряд - 3
# Дано натуральное число n. Напечатайте все n-значные нечетные натуральные
# числа в порядке убывания.

n = int(input())
bottom_limit = 10 ** (n - 1)
if n == 1:
    bottom_limit = 0
print(*[n for n in range(10 ** n - 1, bottom_limit, -1)])
