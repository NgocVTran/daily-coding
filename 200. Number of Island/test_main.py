from unittest import TestCase
from main import Island
from test_data import input_matrices


class TestIsland(TestCase):
    def setUp(self):
        self.Island_1 = Island(input_matrix=input_matrices[0])
        self.Island_2 = Island(input_matrix=input_matrices[1])
        self.Island_3 = Island(input_matrix=input_matrices[2])


class TestInit(TestIsland):

    def test_initial_values(self):
        """
        This function will test initial number of island
        :return: True if nr_of_island equals 0
        """
        self.assertEqual(self.Island_1.nr_of_island, 0, "Initial values of island's number")
        self.assertEqual(self.Island_2.nr_of_island, 0, "Initial values of island's number")
        self.assertEqual(self.Island_3.nr_of_island, 0, "Initial values of island's number")

    def test_matrix_size(self):
        """
        This function will test number of row and columns of input matrix
        """
        # first matrix has 4 rows and 5 columns
        self.assertEqual(self.Island_1.row, 4)
        self.assertEqual(self.Island_1.col, 5)

        # second matrix has 4 rows and 5 columns
        self.assertEqual(self.Island_2.row, 4)
        self.assertEqual(self.Island_2.col, 5)

        # third matrix has 3 rows and 8 columns
        self.assertEqual(self.Island_3.row, 3)
        self.assertEqual(self.Island_3.col, 8)

    def test_result_1(self):
        """
        This function will test result, number of island
        """
        self.assertEqual(self.Island_1.counting_island(), 3, "Test matrix 1")  # first matrix has 3 islands
        self.assertEqual(self.Island_2.counting_island(), 1, "Test matrix 2")  # second matrix has 1 island
        self.assertEqual(self.Island_3.counting_island(), 5, "Test matrix 3")  # second matrix has 5 islands
