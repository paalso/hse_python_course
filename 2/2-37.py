# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/UvmzK/sriednieie-znachieniie-posliedovatiel-nosti

# Среднее значение последовательности
# Определите среднее значение всех элементов последовательности, завершающейся числом 0. 
# Использовать массивы в данной задаче нельзя.

sum = 0
k = 0

while True:
    n = int(input())
    if n == 0:
        break
    sum += n
    k += 1

print(sum / k)
