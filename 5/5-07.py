# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/OIAiF/liesienka/

# Лесенка

# По данному натуральному n≤9 выведите лесенку из n ступенек, i-я ступенька
# состоит из чисел от 1 до i без пробелов.


def print_progression(n):
    for i in range(1, n + 1):
        print(i, end='')
    print()


n = int(input())

for i in range(1, n + 1):
    print_progression(i)
