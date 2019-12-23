# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9Vl6a/oshibki-transponirovaniie

# Ошибки, транспонирование

from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:

    @staticmethod
    def transposed(matrix):
        trans_matrix = []
        width, height = len(matrix.matrix[0]), len(matrix.matrix)
        for i in range(width):
            trans_matrix.append([matrix.matrix[j][i] for j in range(height)])
        return Matrix(trans_matrix)

    def __init__(self, rows):
        self.matrix = deepcopy(rows)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def height(self):
        return len(self.matrix)

    def width(self):
        return len(self.matrix[0])

    def size(self):
        return self.height(), self.width()

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)

        summa = []
        for i in range(self.height()):
            summa.append(
                map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
        return Matrix(summa)

    def __mul__(self, scalar):
        product = []
        for i in range(self.height()):
            product.append(map(lambda x: x * scalar, self.matrix[i]))
        return Matrix(product)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def transpose(self):
        trans_matrix = []
        for i in range(self.width()):
            trans_matrix.append(
                [self.matrix[j][i] for j in range(self.height())]
            )
        self.matrix = deepcopy(trans_matrix)
        return self


exec(stdin.read())
