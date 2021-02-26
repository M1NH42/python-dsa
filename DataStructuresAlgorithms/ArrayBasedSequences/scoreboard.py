class Scoreboard:
    """Fixed lenght sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Inintialize score board with given maximum capacity.
        
        All enteries are initially none.
        """       
        self._board = [None] * capacity # sequence
        self._n = 0 # count number of elements

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Returning string representation of the high score list."""
        return '\n'.join(str(sel._board[k]) for k in range(self._n))

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            
            j = self._n - 1

            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry