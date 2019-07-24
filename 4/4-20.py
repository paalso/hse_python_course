# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/mfqaz/razvorot-posliedovatiel-nosti/submission

# Разворот последовательности
# Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите
# эту последовательность в обратном порядке. При решении этой задачи нельзя
# пользоваться массивами и прочими динамическими структурами данных.Рекурсия
# вам поможет.


def reverse_seq():
    n = int(input())
    if n == 0:
        print(n)
        return
    reverse_seq()
    print(n)


reverse_seq()
