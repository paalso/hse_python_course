# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/uBNr7/sliianiie-spiskov

# Слияние списков

# Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините
# их в один упорядоченный список С (то есть он должен содержать len(A)+len(B)
# элементов). Решение оформите в виде функции merge(A, B), возвращающей новый
# список. Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать
# исходные списки запрещается. Использовать функцию sorted и метод sort нельзя!


def merge(list1, list2):
    merged = []
    i1 = i2 = 0

    while True:
        if i1 == len(list1):
            merged.extend(list2[i2:])
            return merged

        if i2 == len(list2):
            merged.extend(list1[i1:])
            return merged

        if list1[i1] < list2[i2]:
            merged.append(list1[i1])
            i1 += 1
        else:
            merged.append(list2[i2])
            i2 += 1


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(*merge(l1, l2))
