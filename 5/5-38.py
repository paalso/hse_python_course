# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9ND1z/kolichiestvo-sovpadaiushchikh-par

# Количество совпадающих пар

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

data = list(map(int, input().split()))

counter = 0
size = len(data)
for i, el in enumerate(data):
    for j in range(i + 1, size):
        if el == data[j]:
            counter += 1

print(counter)
