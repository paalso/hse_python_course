# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/h1SFz/obuvnoi-maghazin

# Обувной магазин

# В обувном магазине продается обувь разного размера. Известно, что одну пару
# обуви можно надеть на другую, если она хотя бы на три размера больше.
# В магазин пришел покупатель.Требуется определить, какое наибольшее количество
# пар обуви сможет предложить ему продавец так, чтобы он смог надеть их все
# одновременно.


def find_first_suitable_size(data, size):
    if size <= data[0]:
        return 0
    if size > data[len(data) - 1]:
        return -1
    for k in range(1, len(data)):
        if data[k - 1] < size <= data[k]:
            return k


def find_next_index(data, current_index, step=3):
    current_size = data[current_index]
    for i in range(current_index + 1, len(data), 1):
        if data[i] >= current_size + step:
            return i
    return -1


size = int(input())
data = list(map(int, input().split()))
data.sort()

k = find_first_suitable_size(data, size)

if k < 0:
    print(0)
else:
    counter = 1
    while(True):
        next_index = find_next_index(data, k)
        if next_index < 0:
            break
        counter += 1
        k = next_index

    print(counter)
