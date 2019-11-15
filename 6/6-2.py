# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/hCNq3/pieriesiechieniie-mnozhiestv

# Пересечение множеств

# Даны два списка, упорядоченных по возрастанию (каждый список состоит из
# различных элементов).
# Найдите пересечение множеств элементов этих списков, т.е. те числа, которые
# являются элементами обоих списков. Алгоритм должен иметь сложность
# O(len(A)+len(B)).
# Решение оформите в виде функции Intersection(A, B). Функция должна возвращать
# список пересечения данных списков в порядке возрастания элементов.
# Модифицировать исходные списки запрещается.


def Intersection(list1, list2):
    result = []
    i1 = i2 = 0

    while True:
        if i1 == len(list1) or i2 == len(list2):
            return result

        if list1[i1] < list2[i2]:
            i1 += 1
        elif list2[i2] < list1[i1]:
            i2 += 1
        else:
            result.append(list1[i1])
            i1 += 1
            i2 += 1


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(*Intersection(l1, l2))
