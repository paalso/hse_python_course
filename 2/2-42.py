## https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/mNFkq/chisla-fibonachchi

## Числа Фибоначчи
## Последовательность Фибоначчи определяется так:
## F[0] = 0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].
## По данному числу n определите n-е число Фибоначчи F[n].


def fib(n):
    if n < 2:
        return n

    f_prev_prev = 0
    f_prev = 1
    k = 1

    while k < n:
        f = f_prev_prev + f_prev
        f_prev_prev = f_prev
        f_prev = f
        k += 1

    return f


n = int(input())
print(fib(n))
