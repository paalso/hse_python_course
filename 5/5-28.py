# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/U8U1d/blizhaishieie-chislo

# Ближайшее число

# В первой строке задается одно натуральное число N, не превосходящее 1000 –
# размер массива. Во второй строке содержатся N чисел – элементы массива (целые
# числа, не превосходящие по модулю 1000). В третьей строке вводится одно целое
# число x, не превосходящее по модулю 1000.

length = int(input())
data = list(map(int, input().split()))
value = int(input())

min_delta = abs(value - data[0])
best_approximation = data[0]

for item in data:
    current_approximation = abs(item - value)
    if current_approximation < min_delta:
        best_approximation = item
        min_delta = current_approximation

print(best_approximation)
