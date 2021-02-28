class Empty(Exception):
    """Raise exception if priority queue is empty."""
    pass

class PriorityQueueBase:
    """Abstract base class for priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __It__(self, other):
            return self._key < other._key           # compare items based on their keys

    def is_empty(self):
        """Return True if the priority queue is mepty."""
        return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with the binary heap."""
    #------------------ nonpublic behaviour -----------------------------

    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return (2*j + 1)

    def _right(self, j):
        return (2*j + 2)

    def _has_left(self, j):
        return self._left(j) < len(self._data)          # index beyond end of list ?

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements present at indices i and j of an array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)                       # recur at position of parent of the j index
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left                          # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)             # recur at position of small_child

    #--------------------- public behaviours --------------------------------------------
    # def __init__(self):
    #     """Create a new empty Priority Queue."""
    #     self._data = []
    
    def __init__(self, contents=()):
        """Create a new priority queue.

        By default, queue will be empty. If contents is given, it should be as an
        iterable sequence of (k, v) tuple specifying the initial contents.
        """
        self._data = [self._Item(k,v) for k,v in contents]
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)             # start at the parent of the last leaf
        for j in range(start, -1, -1):                  # going to and including the root
            self._downheap(j)

    def __len__(self):
        """Return the number of elements in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a (key, value) pair in the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)           # upheap newly added position

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key.

        Raise empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty!')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty!')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)