# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/dzdH6/xor-2

# XOR - 2

# XOR для произвольного числа аргументов определяется следующим образом:
# xor(a₁,a₂,…,an)= xor(a₁, xor(a₂, xor(a₃,… xor(an))…)
# XOR от n последовательностей A₁,…,An (Aᵢ=Aᵢ₁,…,Aᵢk) равных длин k — это
# последовательность C=xor(A₁,…,An),такая, что: cᵢ=xor(A₁ᵢ,…Anᵢ)
# Посчитайте XOR от n последовательностей равной длины k.

import functools


def xor(*args):
    return functools.reduce(lambda acc, el: acc ^ el, args)


def multy_xor(*arrays):
    return list(map(xor, *arrays))


print(
    *multy_xor(
        *map(
            lambda s: list(map(int, s.split())),
            open('input.txt', 'r').readlines()[1:]
        )
    )
)

##FAIL:
##Precompile check failed:
##not functional enough