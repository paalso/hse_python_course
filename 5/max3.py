# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/OIAiF/liesienka/

# Лесенка

# По данному натуральному n≤9 выведите лесенку из n ступенек, i-я ступенька
# состоит из чисел от 1 до i без пробелов.


def sgn(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0

