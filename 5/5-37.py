# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/HsPIC/naibol-shieie-proizviedieniie-triekh-chisiel

# Наибольшее произведение трех чисел

# В данном списке из n≤10⁵ целых чисел найдите три числа,произведение которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка. То есть сортировку использовать нельзя.
# Выведите три искомых числа в любом порядке.


def insert_in_order_to_max(ordered_list, el):
    for i in range(len(ordered_list) - 1, -1, -1):
        if el > ordered_list[i]:
            for j in range(i):
                ordered_list[j] = ordered_list[j + 1]
            ordered_list[i] = el
            return


def insert_in_order_to_min(ordered_list, el):
    for i in range(len(ordered_list)):
        if el < ordered_list[i]:
            for j in range(len(ordered_list) - 1, i, -1):
                ordered_list[j] = ordered_list[j - 1]
            ordered_list[i] = el
            return


def maximaze_product(data):
    minimals = sorted(data[:3])
    maximals = minimals.copy()

    for i in range(3, len(data)):
        el = data[i]
        if el >= 0:
            insert_in_order_to_max(maximals, el)
        else:
            insert_in_order_to_min(minimals, el)

    print(minimals)
    print(maximals)

##    if maximals[0] * maximals[1] >= minimals[0] * minimals[1]:
##        return tuple(maximals)
##    return tuple(minimals)

s = "5 1 6 99 2 100 100 -2 88 -3"
data = list(map(int, s.split()))
##data = list(map(int, input().split()))

##print(*maximaze_product(data))
maximaze_product(data)
