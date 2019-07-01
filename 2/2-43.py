## https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/eTYuD/nomier-chisla-fibonachchi/submission

## Номер числа Фибоначчи
## Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно
## является, то есть выведите такое число n, что F[n]=A.
## Если А не является числом Фибоначчи, выведите число -1.

def fib_num(n):
    if n < 2:
        return n

    f_prev_prev = 0
    f_prev = 1
    k = 1
    f = 1

    while f < n:
        f = f_prev_prev + f_prev
        f_prev_prev = f_prev
        f_prev = f
        k += 1

    if f == n:
        return k

    return -1


n = int(input())
print(fib_num(n))
