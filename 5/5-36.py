# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/L0BGh/naibol-shieie-proizviedieniie-dvukh-chisiel

# Наибольшее произведение двух чисел

# Дан список, заполненный произвольными целыми числами. Найдите в этом списке
# два числа, произведение которых максимально. Выведите эти числа в порядке
# неубывания.
#
# Решение должно иметь сложность O(n), где n - размер списка. То есть
# сортировку использовать нельзя.


def maximaze_product(data):
    minimals = [min(data[0], data[1]), max(data[0], data[1])]
    maximals = minimals.copy()
##    maximals = [min(data[0], data[1]), max(data[0], data[1])]

    for i in range(2, len(data)):
        el = data[i]
        if el >= 0:
            if el > maximals[1]:
                maximals = [maximals[1], el]
            elif el > maximals[0]:
                maximals[0] = el
        else:
            if el < minimals[0]:
                minimals = [el, minimals[0]]
            elif el < minimals[1]:
                minimals[1] = el

    if maximals[0] * maximals[1] >= minimals[0] * minimals[1]:
        return tuple(maximals)
    return tuple(minimals)


data = list(map(int, input().split()))

print(*maximaze_product(data))
