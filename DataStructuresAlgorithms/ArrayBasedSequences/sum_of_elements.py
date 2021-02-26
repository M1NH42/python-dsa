class CreateTwoDArray:
    """Creates two dimensional array."""

    def __init__(self, row, column):
        """Create a new two dim array."""
        self._row = row
        self._col = column
        self._two_d_list = [[2] * self._col for i in range(self._row)]

    def sum_two_d_array(self):
        """Sum of elements of a two dimensional list/array."""
        sum = 0
        for i in range(self._row):
            for j in range(self._col):
                sum += self._two_d_list[i][j]
        return sum

two_d_array = CreateTwoDArray(3, 3)

print(two_d_array.sum_two_d_array())