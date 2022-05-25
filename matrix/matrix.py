from random import randint
import numpy

MAX_ROWS = MAX_COLUMNS = 5
MAX_NUMBER = 999
MIN_NUMBER = -999
SEQUENCE_LENGTH = 4


class Matrix(object):

    def seed_matrix(self):
        matrix = [[randint(MIN_NUMBER, MAX_NUMBER)
                   for i in range(0, MAX_COLUMNS)]
                  for j in range(0, MAX_ROWS)]
        return matrix

    def print_matrix(self, matrix):
        print(numpy.matrix(matrix))

    def _find_horizontal_sequence(self, matrix):
        curr = False
        for i in range(0, len(matrix)):
            row = matrix[i]
            sequence = []
            for j in range(0, len(row)):
                curr = row[j]
                if len(sequence) == 0:
                    sequence = [curr]
                elif curr == sequence[-1] + 1:
                    sequence.append(curr)
                else:
                    sequence = []
                if len(sequence) == SEQUENCE_LENGTH:
                    return sequence
        return []

    def _transpose_matrix(self, matrix):
        return numpy.transpose(matrix)

    def find_sequence(self, matrix):
        sequence = self._find_horizontal_sequence(matrix)
        if not sequence:
            matrix = self._transpose_matrix(matrix)
            sequence = self._find_horizontal_sequence(matrix)
        return sequence


if __name__ == '__main__':
    matrix_obj = Matrix()
    matrix = matrix_obj.seed_matrix()
    matrix_obj.print_matrix(matrix)
    sequence = matrix_obj.find_sequence(matrix)
    if sequence:
        print('First: %i' % sequence[0])
        print('Last: %i' % sequence[-1])
