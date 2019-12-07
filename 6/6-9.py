# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/66PkM/sortirovka-podschietom

# Сортировка подсчетом
# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения
# от 0 до 100.
# Отсортируйте этот список в порядке неубывания элементов. Выведите полученный
# список. Решение оформите в виде функции CountSort(A), которая модифицирует
# передаваемый ей список. Использовать встроенные функции сортировки нельзя.


def CountSort(lst, qty=100):
    tmpList = [0] * (qty + 1)
    for el in lst:
        tmpList[el] += 1

    i = k = 0
    while k < len(lst):
        for j in range(tmpList[i]):
            lst[k] = i
            k += 1
        i += 1


data = list(map(int, input().split()))
CountSort(data)
print(*data)
