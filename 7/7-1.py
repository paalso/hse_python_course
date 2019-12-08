# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ghZju/kolichiestvo-sovpadaiushchikh/submission

# Количество различных чисел

# Дан список чисел, который может содержать до 100000 чисел.Определите, сколько
# в нем встречается различных чисел.

print(len(set(map(int, input().split()))))
