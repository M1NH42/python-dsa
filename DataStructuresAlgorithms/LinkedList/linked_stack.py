class Empty(Exception):
    """Raise Empty exception if the stack is empty or has no elmeent in it."""
    pass
class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    #-------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #------------------------- stack methods ------------------------
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        """Return the number of lements in the stack."""
        return self._size
    
    def is_empty(self):
        """Return true if stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._head._element

    def pop(self):
        """Remove and return the element at the top of the stack (i.e., LIFO)

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def print_stack(self):
        while self._head != None:
            print(self._head._element)
            self._head = self._head._next

#--------------- TEST THE ABOVE CODE -------------------
L = LinkedStack()
L.push(2)
L.push(3)
L.push(4)
L.push(5)
L.push(8)
L.push(1)
L.print_stack()
# L.pop()
print('Total number of elements in stack:', L.__len__())
print()
L.print_stack()
print(L.is_empty())
# print('*******************************')
# print(L.top())
# top_element = L.top()
# print(top_element)
L.pop()