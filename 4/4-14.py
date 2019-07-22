# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/lf4m0/bystroie-vozviedieniie-v-stiepien/submission

# Быстрое возведение в степень
# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм
# быстрого возведения в степень. Если вы все сделаете правильно,то сложность
# вашего алгоритма будет O(logn).


def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return power(a, b // 2) ** 2
    return power(a, b - 1) * a


a = float(input())
b = int(input())

print(power(a, b))
