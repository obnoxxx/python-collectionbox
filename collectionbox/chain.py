"""
Chain class/ chain module of the collectionbox package
This implements the doubly linked list class Chain using the internal _DlNode class.
"""

"""
_DlNode is the nternal node representation of a node  for the doubly linked list class (Chain).
It is hidden from consumers of Chain.
"""


class _DlNode:
    def __init__(self, data, _prev=None, _next=None):
        """
        By default, sart with a node that is not connected
        """
        self.__next = _next
        self.__prev = _prev
        self.__data = data

    # setter and getter mothods for the (private attributes:
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, node):
        self.__prev = node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Chain:
    """
    Chain() creates an empty list by default. An optional iterable or
    non-iterable single value initializes the chain with its values.
    """

    _MISSING = object()

    def __init__(self, value_or_iterable=_MISSING):

        self.__head = None
        self.__tail = None
        self.__size = 0
        if value_or_iterable is not Chain._MISSING:
            self += value_or_iterable

    @property
    def head(self):
        return None if self.__head is None else self.__head.data

    @head.setter
    def head(self, data):
        if self.__head is None:
            self.append(data)
        else:
            self.__head.data = data

    @property
    def tail(self):
        return None if self.__tail is None else self.__tail.data

    @tail.setter
    def tail(self, data):
        if self.__tail is None:
            self.append(data)
        else:
            self.__tail.data = data

    def __iter__(self):
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def __reversed__(self):
        current = self.__tail
        while current:
            yield current.data
            current = current.prev

    def __len__(self):
        return self.__size

    def __getitem__(self, idx):
        return self._get_node(idx).data

    def __setitem__(self, idx, data):
        self._get_node(idx).data = data

    def __repr__(self):
        return f"DlList({list(self)})"

    def extend(self, iterable):
        if iterable is self:
            iterable = list(iterable)
        for item in iterable:
            self.add(item)

    # implement += ...:
    def __iadd__(self, other):
        if other is self:
            self.extend(other)
            return self

        try:
            iterator = iter(other)
        except TypeError:
            self.add(other)
        else:
            self.extend(iterator)
        return self

    def copy(self):
        new = Chain()
        new += self
        return new

    # implement +:...
    def __add__(self, other):
        new = self.copy()
        new += other
        return new

    def len(self):
        return self.__size

    # Return the index of the first node with the given data.
    # Returns -1 if the data is not found.
    def index(self, data):
        idx = 0
        node = self.__head
        while node is not None:
            if node.data == data:
                return idx
            idx += 1
            node = node.next
        # not found: indicated by -1
        return -1

    # remove a given node from the list
    def _remove_node(self, node):
        if node is None:
            return
        previous = node.prev
        following = node.next
        if previous is None:
            self.__head = following
        else:
            previous.next = following
        if following is None:
            self.__tail = previous
        else:
            following.prev = previous
        self.__size -= 1

    def remove_at(self, index):
        """
        remove node at given index
        """
        self._remove_node(self._get_node(index))

    def remove(self, data):
        """
        remove removes the first node with the given data.
        """
        node = self.__head
        while node is not None and node.data != data:
            node = node.next
        self._remove_node(node)

    # number of nodes with this data.
    def count(self, data):
        num = 0
        node = self.__head
        while node is not None:
            if node.data == data:
                num += 1
            node = node.next
        return num

    # remove all nodes with this data.
    def remove_all(self, data):
        node = self.__head
        while node is not None:
            next_node = node.next
            if node.data == data:
                self._remove_node(node)
            node = next_node

    def prepend(self, data):
        """
        Add a data node to the beginning of the list.
        """
        new_node = _DlNode(data)
        new_node.next = self.__head
        if self.__head is None:
            self.__tail = new_node
        else:
            self.__head.prev = new_node
        self.__head = new_node
        self.__size += 1

    def append(self, data):
        """
        Add a data node to the end of the list.
        """
        new_node = _DlNode(data)
        new_node.prev = self.__tail
        if self.__tail is None:
            self.__head = new_node
        else:
            self.__tail.next = new_node
        self.__tail = new_node
        self.__size += 1

    def add(self, data):  # alias for append
        self.append(data)

    def _index_is_in_bounds(self, idx):
        return idx >= 0 and idx < self.__size

    def _get_node(self, idx):
        if not self._index_is_in_bounds(idx):
            raise IndexError("list index out of range")
        i = 0
        node = self.__head
        while i < idx:
            node = node.next
            i += 1
        return node

    def _replace_node_with_node(self, node, new_node):
        if node is None:
            return
        if new_node is None:
            return
        previous = node.prev
        following = node.next
        new_node.next = following
        new_node.prev = previous
        if previous is None:
            self.__head = new_node
        else:
            previous.next = new_node
        if following is None:
            self.__tail = new_node
        else:
            following.prev = new_node

    def _insert(self, idx, data):
        """
        insert an item before the given index.
        - internal implementation
        """
        new_node = _DlNode(data)
        node = self._node_at(idx)
        if node is None:
            return False
        previous = node.prev
        next = node.next
        new_node.next = node
        new_node.prev = previous
        node.prev = new_node
        if previous is None:
            self.__head = new_node
        else:
            previous.next = new_node
        self.__size += 1

    def insert(self, index, data):
        """
        Insert an item before the given index.
        - public interface
        """
        self._insert(index, data)

    def clear(self):
        """
        drain the entire list
        """
        self.__head = None
        self.__tail = None
        self.__size = 0
