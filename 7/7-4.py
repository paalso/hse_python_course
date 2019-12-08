# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/URmWN/vstriechalos-li-chislo-ran-shie

# Встречалось ли число раньше

# Во входной строке записана последовательность чисел через пробел. Для каждого
# числа выведите слово YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если не встречалось.

data = list(map(int, input().split()))

unique = set()
for num in data:
    if num not in unique:
        print('NO')
        unique.add(num)
    else:
        print('YES')
