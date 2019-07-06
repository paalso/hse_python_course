# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/dCRo6/naimien-shieie-rasstoianiie-miezhdu-lokal-nymi-maksimumami/submission

# Наименьшее расстояние между локальными максимумами
# Определите наименьшее расстояние между двумя локальными максимумами
# последовательности натуральных чисел, завершающейся числом 0. Локальным
# максимумом называется такое число в последовательности, которое больше
# своих соседей. Если в последовательности нет двух локальных максимумов,
# выведите число 0. Начальное и конечное значение при этом локальными
# максимумами не считаются.

n_prev_prev = int(input())
n_prev = int(input())
max_counter = 0
min_dist = 0
pos = 1

while True:
    n = int(input())
    pos += 1
    if n == 0:
        break

    if n < n_prev > n_prev_prev:
        max_last_pos = pos - 1
        max_counter += 1
        if max_counter == 1:
            max_prev_pos = max_last_pos
            n_prev_prev = n_prev
            n_prev = n
            continue

        if max_counter == 2:
            min_dist = max_last_pos - max_prev_pos
            max_prev_pos = max_last_pos
        else:
            last_dist = max_last_pos - max_prev_pos
            max_prev_pos = max_last_pos
            if last_dist < min_dist:
                min_dist = last_dist

    n_prev_prev = n_prev
    n_prev = n

print(min_dist)
