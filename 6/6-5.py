# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/XWi6G/sozdaniie-arkhiva

# Создание архива

# Системный администратор вспомнил, что давно не делал архива пользовательских
# файлов. Однако, объем диска, куда он может поместить архив, может быть меньше
# чем суммарный объем архивируемых файлов.
# Известно, какой объем занимают файлы каждого пользователя.
#
# Напишите программу, которая по заданной информации о пользователях и
# свободному объему на архивном диске определит максимальное число
# пользователей, чьи данные можно поместить в архив.


total_size, users = tuple(map(int, input().split()))
data = []

for i in range(users):
    data.append(int(input()))

data.sort()

s = 0
for i, size in enumerate(data):
    s += size
    if s > total_size:
        break
else:
    i += 1

print(i)
