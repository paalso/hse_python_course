# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/mfqaz/razvorot-posliedovatiel-nosti/submission

# Теорема Лагранжа
# Теорема Лагранжа утверждает, что любое натуральное число можно представить в
# виде суммы четырех точных квадратов. По данному числу n найдите такое
# представление: напечатайте от 1 до 4 натуральных чисел, квадраты которых дают
# в сумме данное число.

from math import sqrt

n = int(input())

for i in range(int(sqrt(n)) + 1):
    for j in range(int(sqrt(n - i * i)) + 1):
        for k in range(int(sqrt(n - i * i - j * j)) + 1):
            rest = n - i * i - j * j - k * k
            l = int(sqrt(rest))
            if l * l == rest:
                solution = (i, j, k, l)
                print(*[num for num in solution if num != 0])
                exit()
