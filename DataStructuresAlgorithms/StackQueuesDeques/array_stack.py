class Empty(Exception):
    """Error attempting to access an element from an empty stack."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a python list as underlying storage."""

    def __init__(self):
        """Create new empty stack."""
        self._data = []     # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return true if stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add lements e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise exception if stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove nad return the element from the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

# S = ArrayStack()
# S.push(12)
# S.push(78)
# S.push(23)

# print('Element present at the top:', S.top())
# print(S.pop())
# print(S.pop())
# print(S.pop())
# # print(S.pop())

def is_matched(expr):
    """Return True if all the delimiters are properly match. False otherwise."""
    lefty = '('
    righty = ')'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

# matched = is_matched('[({})]')
matched = is_matched('(5+x)-(y+z)')
print(matched)