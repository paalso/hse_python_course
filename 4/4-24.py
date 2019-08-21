# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/1NUN8/tol-ko-kvadraty/submission

# Только квадраты
# Напишите программу, которая выбирает из полученной последовательности квадраты
# целых чисел выводит их в обратном порядке. Использовать массив для хранения
# последовательности не разрешается.


def print_sqrs(counter):
    n = int(input())
    if n == 0:
        print(f"counter in: {counter}")
        return counter

    was_sqrt = False
    q = int(n ** 0.5)
    if q * q == n:
        was_sqrt = True

    print_sqrs(counter + int(was_sqrt))

    if was_sqrt:
        print(n, end=' ')


x = print_sqrs(0)
print(f"counter out: {x}")
if x == 0:
    print(0)
