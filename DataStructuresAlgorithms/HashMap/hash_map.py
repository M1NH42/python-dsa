# Extending the MutableMapping abstract base class to provide a nonpblic _Item
# class for use in various map implementation
from collections.abc import MutableMapping


class MapBase(MutableMapping):
    """Our own abstract base class tha includes a nonpublic _Item class."""

    # --------------------- nested _Item class -----------------------------
    class _Item:
        """Lightweight composite to store key-value pair as items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)              # opposite of the __eq__()

        def __It__(self, other):
            return self._key < other._key           # compare based on their keys


class UnsortedTableMap(MapBase):
    """Map implementation using an unsorted list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []                            # list of _Items

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
            return
        # did not find match for the key
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with the k (raise KetError if not found)"""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error:' + repr(k))

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of map keys"""
        for item in self._table:
            yield item._key


class HashMapBase(MapBase):
    """Astract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash table map."""
        self._table
