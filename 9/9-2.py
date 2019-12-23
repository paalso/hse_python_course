# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/cTJex/dobavit-umnozhit

# Добавить, умножить

from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, rows):
        self.matrix = deepcopy(rows)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        summa = []
        for i in range(self.size()[0]):
            summa.append(
                map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
        return Matrix(summa)

    def __mul__(self, scalar):
        product = []
        for i in range(self.size()[0]):
            product.append(map(lambda x: x * scalar, self.matrix[i]))
        return Matrix(product)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)


exec(stdin.read())
