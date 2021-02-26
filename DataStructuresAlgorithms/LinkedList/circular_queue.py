class Empty(Exception):
    pass

class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty!')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty!')
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

    # def print_circular_q(self):
    #     _current = self._tail
    #     while _current._element != self._tail._element:
    #         print(self._tail._element)
    #         self._tail = self._tail._next
# ************ TEST CODE ****************
C = CircularQueue()
C.enqueue(3)
C.enqueue(6)
C.enqueue(0)
print('First element in the circular q:', C.first())
C.dequeue()
print('First element in the circular q:', C.first())
# C.print_circular_q()