# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/Z8IA2/maksimum-posliedovatiel-nosti

# Максимум последовательности
# Последовательность состоит из целых чисел и завершается числом 0. 
# Определите значение наибольшего элемента последовательности.

n = int(input())
max = n

while n != 0:
    n = int(input())
    if max < n:
        max = n

print(max)
