class Empty(Exception):
    """Raise error accessing element from the mepty queue."""
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty!')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue i empty!')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # shrinking the underlying array
        # START
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2) # END
        return answer

    def enqueue(self, e):
        """Add element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))       # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):             # we assume cap >= len(self)
        """Resize to a new list of capacity > len(self)."""
        old = self._data        # keep track of existing list
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

# TEST ABOVE CODE:
Q = ArrayQueue()
Q.enqueue(2)
Q.enqueue(5)
Q.enqueue(8)
first_element = Q.first()
print('Number of elements in the queue:', Q.__len__())
print('The first element is the first pass:', first_element)
Q.dequeue()
first_element = Q.first()
print('Number of elements in the queue:', Q.__len__())
print('The first element in the second pass:', first_element)
Q.dequeue()
first_element = Q.first()
print('Number of elements in the queue:', Q.__len__())
print('The first element in the third pass:', first_element)
Q.dequeue()
# first_element = Q.first()
# print('The first element in the fourth pass:', first_element)
# Q.dequeue()