# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/5eh7t/chisla-fibonachchi

# Числа Фибоначчи
# Напишите функцию phib(n), которая по данному целому неотрицательному n
# возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы -
# используйте рекурсию.


def phib(n):
    if n < 2:
        return n
    return phib(n - 1) + phib(n - 2)


n = int(input())
print(phib(n))
