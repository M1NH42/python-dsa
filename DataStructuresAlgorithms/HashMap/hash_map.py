# Extending the MutableMapping abstract base class to provide a nonpblic _Item
# class for use in various map implementation
class MapBase(MutableMpping):
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
