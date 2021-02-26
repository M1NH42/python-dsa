class Empty(Exception):
    pass

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

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #---------------------- nested Position class -----------------------
    class Position:
        """An abstracttion representing the location of a single eleemnt."""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user."""
            self._container = container
            self._node = node

        def element(self):
            """Return element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if the oher is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)          # opposite of __eq__

    #---------------------- utility method -----------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:           # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    #---------------------- utility method -----------------------
    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinels)."""
        if node is self._header or node is self._trailer:
            return None                                         # boundary validation
        else:
            return self.Position(self, node)

    #---------------------- accessor ----------------------------
    def first(self):
        """Return the first position in the list. (or None if the list is empty.)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if the list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if the p is the first node)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the position just after Position p (or NOne if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #---------------------- mutators -----------------------
    # override inherited version to return Position, rather than node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing node and return the new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formely at Position p.
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

# *************************** PRIORITY QUEUE IMPL *********************************************
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

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):                # non-public utility
        """Return position of the item with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty!')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new Empty Priority queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return number of elements in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Return and remove (k, v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

# P = UnsortedPriorityQueue()
# print(P.is_empty())
# P.add(3, 4)
# P.add(1, 3)
# print(P.is_empty())
# print('Number of items in PQ:', P.__len__())
# print(P.min())

class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        if self.is_empty():
            raise Empty('Priority queue is mepty1')
        newest = self._Item(key, value)
        walk = self._data.last()                # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove the item with minimum key in the list."""
        if self.is_empty():
            raise Empty('Priority queue is empty!')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Return and remove the item with minimum key in the list."""
        if self.is_empty():
            raise Empty('Priority queue is empty!')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

P = SortedPriorityQueue()
print(P.is_empty())
P.add(0, 4)
P.add(1, 3)
P.add(2, 1)
P.add(3, 0)
print(P.is_empty())
print('Number of items in PQ:', P.__len__())
P.min()