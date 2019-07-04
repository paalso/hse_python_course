# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/6I71w/maksimal-noie-chislo-podriad-idushchikh-ravnykh

# Максимальное число подряд идущих равных
# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой
# последовательности равны друг другу.

n = int(input())
n_prev = n
curent_len = 1
total_max = 1

while n != 0:
    n = int(input())
    if n == n_prev:
        curent_len += 1
        if curent_len > total_max:
            total_max = curent_len
    else:
        curent_len = 1

    n_prev = n

print(total_max)
