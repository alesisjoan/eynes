import unittest
from random import randint
from matrix import Matrix
from matrix import MAX_ROWS, MAX_COLUMNS


class TestMatrix(unittest.TestCase):

    def _get_random_row(self, matrix):
        return matrix[randint(0, (MAX_ROWS - 1))]

    def test_matrix(self):
        """
        Test can generate a matrix of integers
        """
        matrix = Matrix().seed_matrix()
        Matrix().print_matrix(matrix)
        self.assertEqual(len(matrix), MAX_COLUMNS)
        self.assertEqual(len(matrix[0]), MAX_ROWS)

        m1 = self._get_random_row(matrix)
        self.assertTrue(type(m1[0]) == int)
        self.assertTrue(type(m1[-1]) == int)
        self.assertTrue(type(m1[int(len(m1) / 2)]) == int)

    def test_find_sequence(self):
        """
        Test find horizontal or vertical sequences
        """

        def _check_sequence(sequence):
            for i in range(0, len(sequence) - 1):
                self.assertTrue(sequence[i] < sequence[i + 1])

        matrixh = [[1, 3, 5, 6, 7], [-5, -4, -3, -2, 8], [5, 4, 3, 6, 7],
                   [9, 6, 5, 4, 2], [4, 3, 2, 6, 7]]
        sequenceh = Matrix().find_sequence(matrixh)
        _check_sequence(sequenceh)
        self.assertEqual(sequenceh, [-5, -4, -3, -2])
        matrixv = [[2, 3, 5, 6, 6], [2, 3, 2, 5, 7], [3, 4, 3, 6, 8],
                   [4, 6, 5, 4, 9], [4, 3, 2, 6, 7]]
        sequencev = Matrix().find_sequence(matrixv)
        _check_sequence(sequencev)
        self.assertEqual(sequencev, [6, 7, 8, 9])
        # negative testing
        matrixn = [[1, 3, 5, 6, 6], [2, 2, 2, 5, 7], [3, 4, 3, 6, 8],
                   [1, 6, 5, 4, 7], [5, 3, 2, 5, 9]]
        nonsequence = Matrix().find_sequence(matrixn)
        self.assertFalse(nonsequence)

    def main(self):
        self.test_matrix()
        self.test_find_sequence()


if __name__ == '__main__':
    unittest.main()
