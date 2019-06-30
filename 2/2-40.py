# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/4pohA/vtoroi-maksimum

# Второй максимум
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим, если из последовательности удалить
# одно вхождение наибольшего элемента.

n = int(input())
max = n

n = int(input())
if n > max:
    sub_max = max
    max = n
else:
    sub_max = n

while n != 0:
    n = int(input())
    if n >= max:
        sub_max = max
        max = n
    elif n > sub_max:
        sub_max = n

print(sub_max)
