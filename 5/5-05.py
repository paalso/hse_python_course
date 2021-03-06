# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/jqFOL/flaghi/submission

# Флаги

# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n
# флагов. Изображение одного флага имеет размер 4×4 символов, между двумя
# соседними флагами также имеется пустой (из пробелов) столбец. Разрешается
# вывести пустой столбец после последнего флага. Внутри каждого флага должен
# быть записан его номер — число от 1 до n.

# +___ +___ +___
# |1 / |2 / |3 /
# |__\ |__\ |__\
# |    |    |


def print_flag(n):
    print('+___ ' * n)
    for k in range(n):
        print(f"|{k + 1} / ", end='')
    print()
    print('|__\\ ' * n)
    print('|    ' * n)


n = int(input())
print_flag(n)
