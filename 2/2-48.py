# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7AoX7/maksimal-naia-dlina-monotonnogho-fraghmienta/submission

# Максимальная длина монотонного фрагмента
# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите наибольшую длину монотонного фрагмента последовательности
# (то есть такого фрагмента, где все элементы либо больше предыдущего,
# либо меньше).

n = int(input())
n_prev = n
inc_len = 1
max_inc_len = 1
dec_len = 1
max_dec_len = 1

while True:
    n = int(input())
    if n == 0:
        break
    if n > n_prev:
        inc_len += 1
        dec_len = 1
        if inc_len > max_inc_len:
            max_inc_len = inc_len
    elif n < n_prev:
        dec_len += 1
        inc_len = 1
        if dec_len > max_dec_len:
            max_dec_len = dec_len
    else:
        inc_len = 1
        dec_len = 1
    n_prev = n

print(max(max_inc_len, max_dec_len))