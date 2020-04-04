# Number of Island
from test_data import input_matrices


class Island():
    def __init__(self, input_matrix):
        self.input_matrix = input_matrix
        self.row = len(input_matrix)        # number of matrix row
        self.col = len(input_matrix[0])     # number of matrix column
        self.nr_of_island = 0

    def counting_island(self):
        """
        This main algorithm function will take input with format:
        input_matrix = List[ List[int] ]

        and return number of island.
        :return: nr_of_island
        """
        for i in range(self.row):
            for j in range(self.col):
                if self.input_matrix[i][j] == 1:
                    self.nr_of_island += 1
                    self.explore(i, j)
        return self.nr_of_island

    def explore(self, i, j):
        """
        This function will check area around position (i,j)
        If this area is a land, it will be marked as visited
        :param i: row i of the input matrix
        :param j: column j of the input matrix
        """
        # initial list of surrounding land
        expand_area = []
        expand_area.append([i, j])

        while expand_area:
            x, y = expand_area.pop()

            self.input_matrix[x][y] = 0      # mark current position as visited
            # add land around current position to this list until only water around
            self.check_neighbour(expand_area, x, y)

    def check_neighbour(self, expand_area, x, y):
        """
        This function will check lef, right, above and under current position
        if they're a land or water
        :param expand_area: list of land
        :param x: current position in x-axis
        :param y: current position in y-axis
        """
        # check left and right position
        if (x + 1 < self.row) and (self.input_matrix[x + 1][y] == 1):
            expand_area.append([x + 1, y])
        if (x - 1 >= 0) and (self.input_matrix[x - 1][y] == 1):
            expand_area.append([x - 1, y])

        # check above and under position
        if (y + 1 < self.col) and (self.input_matrix[x][y + 1] == 1):
            expand_area.append([x, y + 1])
        if (y - 1 >= 0) and (self.input_matrix[x][y - 1] == 1):
            expand_area.append([x, y - 1])


if __name__ == "__main__":
    for i in range(len(input_matrices)):
        print("Total number of Island(s) in matrix {}: {}"
              .format(i+1, Island(input_matrices[i]).counting_island()))
