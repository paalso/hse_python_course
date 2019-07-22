# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/cxeHQ/vozviedieniie-v-stiepien/submission

# Возведение в степень
# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите aⁿ, не используя циклы и стандартную функцию pow, но используя
# рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
# Решение оформите в виде функции power(a, n) (которая возвращает aⁿ).


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

a = float(input())
n = int(input())

print(power(a, n))
