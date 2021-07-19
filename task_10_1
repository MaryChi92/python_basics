import numpy


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix = '\n'.join(' '.join(map(str, i)) for i in self.matrix_list)
        return matrix

    def __add__(self, other):
        new_matrix = self.matrix_list + other.matrix_list
        return new_matrix


matrix_1 = Matrix(numpy.array([[5, 3, -1], [17, 6, 8], [9, -5, 0]]))
matrix_2 = Matrix(numpy.array([[10, 3, 0], [-15, -9, 7], [4, 2, 11]]))
print(matrix_1)
print('-' * 30)
print(matrix_2)
print('-' * 30)
print(matrix_1 + matrix_2)
