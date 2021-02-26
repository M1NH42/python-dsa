class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._element = node._prev = node._next = None
        return element

class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Empt deque!')
        return self._trailer._prev._element

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)     # before trailer

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)       # after header

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._delete_node(self._header._next)        # use inherited method

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty!!')
        return self._delete_node(self._trailer._prev)       # use inherited method