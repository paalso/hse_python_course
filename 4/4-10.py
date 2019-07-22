# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ktpvw/provierka-chisla-na-prostotu

# Проверка числа на простоту
# Дано натуральное число n>1. Проверьте, является ли оно простым. Программа
# должна вывести слово YES, если число простое и NO, если число составное.
# Решение оформите в виде функции IsPrime(n), которая возвращает True для
# простых чисел и False для составных чисел. Программа должна иметь сложность
# O(корень из n): количество действий в программе должно быть пропорционально
# квадратному корню из n (иначе говоря, при увеличении входного числа в k раз,
# время выполнения программы должно увеличиваться примерно в корень из k раз).


def PrintAnswer(predicate, yesAnswer="YES", noAnswer="NO"):
    if(predicate):
        print(yesAnswer)
    else:
        print(noAnswer)


def MinDivisor(n):
    if n & 1 == 0:
        return 2
    upper_lim = int(n ** 0.5)
    k = 3
    while k <= upper_lim:
        if n % k == 0:
            return k
        k += 2
    return n


def IsPrime(n):
    if n == 1:
        return False
    return MinDivisor(n) == n


n = int(input())
PrintAnswer(IsPrime(n))
