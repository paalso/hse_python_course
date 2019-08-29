# Теорема Лагранжа
# Теорема Лагранжа утверждает, что любое натуральное число можно представить
# в виде суммы четырех точных квадратов. По данному числу n найдите такое
# представление: напечатайте от 1 до 4 натуральных чисел, квадраты которых дают
# в сумме данное число.


def print_without_zeros(t):
    for n in t:
        if n != 0:
            print(n, end = ' ')
    print()


def lagrange(n):
    lim = int(n ** 0.5)
    for i in range(lim, -1, -1):
        for j in range(n - i * i, -1, -1):
            for k in range(n - i * i - j * j, -1, -1):
                sum_three_squares = i * i + j * j + k * k
                last = n - sum_three_squares
                if last < 0:
                    break
                last = int(last ** 0.5)
                if sum_three_squares + last * last == n:
                        return (i, j, k, last)


##n = int(input())
##print_without_zeros(lagrange(n))

##for i in range(1,10):
##    print(i, end = '   ')
##    print_without_zeros(lagrange(i))


for i in range(1,10):
    print(lagrange(i))