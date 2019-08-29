# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/Qm8Xr/kolichiestvo-nuliei/submission

# Количесто нулей

# Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите
# это количество.

n = int(input())
counter = 0
for i in range(n):
    next = int(input())
    if next == 0:
        counter += 1
print(counter)
