# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/1NUN8/tol-ko-kvadraty/submission

# Только квадраты
# Напишите программу, которая выбирает из полученной последовательности квадраты
# целых чисел выводит их в обратном порядке. Использовать массив для хранения
# последовательности не разрешается.

counter = 0


def print_sqrs():
    global counter
    n = int(input())
    if n == 0:
        return 0
    print_sqrs()
    q = int(n ** 0.5)
    if q * q == n:
        print(n, end=' ')
        counter += 1


print_sqrs()
if counter == 0:
    print(0)
