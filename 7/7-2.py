# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ghZju/kolichiestvo-sovpadaiushchikh

# Количество совпадающих

# Даны два списка чисел, которые могут содержать до 100000 чисел каждый.
# Посчитайте, сколько чисел содержится одновременно как в первом списке,
# так и во втором.

print(len(set(map(int, input().split())) & set(map(int, input().split()))))
