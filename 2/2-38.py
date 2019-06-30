# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/iNgy8/kolichiestvo-chietnykh-eliemientov-posliedovatiel-nosti/submission

# Количество четных элементов последовательности
# Определите количество четных элементов в последовательности, завершающейся числом 0.

k = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        k += 1

print(k)