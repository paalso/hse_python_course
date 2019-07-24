# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/NiOd7/summa-posliedovatiel-nosti/submission

# Сумма последовательности
# Дана последовательность чисел, завершающаяся числом 0. Найдите сумму всех
# этих чисел, не используя цикл.


def sum_seq():
    n = int(input())
    if n == 0:
        return 0
    return n + sum_seq()


print(sum_seq())
