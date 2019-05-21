# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9G2HO/minimal-nyi-dielitiel/submission

# Минимальный делитель
# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

def minimalDivisor(n):
    if (n % 2 == 0):
        return 2

    sqrt = int(n ** 0.5)
    divisor = 3

    while (divisor <= sqrt):
        if(n % divisor == 0):
            return divisor

        divisor += 2

    return n

n = int(input())
print(minimalDivisor(n))
