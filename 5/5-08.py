# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7PClq/zamiechatiel-nyie-chisla-1/submission

# Замечательные числа - 1

# Найдите и выведите все двузначные числа, которые равны удвоенному
#  произведению своих цифр.


def digits_product(n: int) -> int:
    """ Сalculates product of digits of a number """
    if n == 0:
        return 0

    product = 1
    while n > 0:
        digit = n % 10
        if digit == 0:
            return 0
        product *= digit
        n //= 10
    return product


for n in range(11, 99):
    if n == 2 * digits_product(n):
        print(n, end=' ')
