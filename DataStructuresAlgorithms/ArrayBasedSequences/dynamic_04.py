import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an mpty array."""
        self._n = 0
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightwards."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, k, -1):
            self._A[i] = self._A[i-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurence of a value (or raise an exception)."""
        for i in range(self._n):
            if self._A[i] == value:
                for j in range(i, self._n - 1):     # shift others to fill the gap
                    self._A[j] = self._A[j+1]       
                self._A[self._n - 1] = None     # help garbage collection
                self._n -= 1    # we have one less item
                return      # return immediately
        raise ValueError('value not found')     # only reached if no match

    