# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/kX4tZ/dlina-posliedovatiel-nosti

# Сумма последовательности
# Определите сумму всех элементов последовательности, завершающейся числом 0.

sum = 0

while True:
    n = int(input())
    if n == 0:
        break
    sum += n

print(sum)

