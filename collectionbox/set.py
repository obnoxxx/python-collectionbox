"""
This is the set/Set module/Class of the  collectionbox package.
"""

from collectionbox import Chain


class Set:
    def __init__(self, iterable=None):
        self._chain = Chain()
        if iterable is not None:
            for item in iterable:
                self.add(item)

    def __len__(self):
        return len(self._chain)

    def __bool__(self):
        return len(self) > 0

    def __repr__(self):
        if not self:
            return "{}"
        return "{" + ", ".join(repr(value) for value in self) + "}"

    def __contains__(self, element):
        return element in self._chain

    def __iter__(self):
        return iter(self._chain)

    def add(self, value):
        if value not in self:
            self._chain.add(value)

    def remove(self, value):
        if value not in self:
            raise KeyError(value)
        self._chain.remove(value)

    def discard(self, element):
        try:
            self.remove(element)
        except KeyError:
            pass

    def clear(self):
        self._chain.clear()
