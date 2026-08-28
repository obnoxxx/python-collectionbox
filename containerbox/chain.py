"""
Chain class/ chain module of the containerbox package
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
    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def get_prev(self):
        return self.__prev

    def set_prev(self, node):
        self.__prev = node

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def is_first(self):
        if self.__prev is None and self.__next is not None:
            return True
        else:
            return False

    def is_last(self):
        if self.__next is None and self.__prev is not None:
            return True
        else:
            return False


#    def prepend(self, node):
#        if node is None:
#            return
#        # can only prepend before the first node
#        if self.is_first():
#            return
#        if self.get_prev() is None:
#            return
#        self.get_prev().set_next(node)
#        self.set_prev(node)
#        node.set_prev(self.get_prev())
#        node.set_next(self)
#    def append(self, node):
#        if node is None:
#            return
#        if self.is_last():
#            return
#        if self.get_next() is None:
#            return
#        self.get_next().set_prev(node)
#        self.set_next(node)
#        node.set_next(self.get_next())
#
#    def get_first(self):
#            node = self
#            while(not node.is_first()):
#                node = node.get_prev()
#            return node
#    def ret_last(self):
#            node = self
#            while(not node.is_last()):
#                node = node.get_next()
#            return node


class Chain:
    """
    Chain() creates an empty list by default.
    """

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_head(self):
        return None if self.__head is None else self.__head.get_data()

    def get_tail(self):
        return None if self.__tail is None else self.__tail.get_data()

    def __iter__(self):
        current = self.__head
        while current:
            yield current.get_data()
            current = current.get_next()

    def __reversed(self):
        current = self.__tail
        while current:
            yield current.get_data()
            current = current.get_prev()

    def __len__(self):
        return self.__size

    def __getitem__(self, idx):
        return self._get_node(idx).get_data()

    def __setitem__(self, idx, data):
        self._get_node(idx).set_data(data)

    def __iadd__(self, iterable):
        for item in iterable:
            self.append(item)
        return self

    def __repr__(self):
        return f"DlList({list(self)})"

    def len(self):
        return self.__size

    # Return the index of the first node with the given data.
    # Returns -1 if the data is not found.
    def index(self, data):
        idx = 0
        node = self.__head
        while node is not None:
            if node.get_data() == data:
                return idx
            idx += 1
            node = node.get_next()
        # not found: indicated by -1
        return -1

    # remove a given node from the list
    def _remove_node(self, node):
        if node is None:
            return
        previous = node.get_prev()
        following = node.get_next()
        if previous is None:
            self.__head = following
        else:
            previous.set_next(following)
        if following is None:
            self.__tail = previous
        else:
            following.set_prev(previous)
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
        while node is not None and node.get_data() != data:
            node = node.get_next()
        self._remove_node(node)

    # number of nodes with this data.
    def count(self, data):
        num = 0
        node = self.__head
        while node is not None:
            if node.get_data() == data:
                num += 1
            node = node.get_next()
        return num

    # remove all nodes with this data.
    def remove_all(self, data):
        node = self.__head
        while node is not None:
            next_node = node.get_next()
            if node.get_data() == data:
                self._remove_node(node)
            node = next_node

    def prepend(self, data):
        """
        Add a data node to the beginning of the list.
        """
        new_node = _DlNode(data)
        new_node.set_next(self.__head)
        if self.__head is None:
            self.__tail = new_node
        else:
            self.__head.set_prev(new_node)
        self.__head = new_node
        self.__size += 1

    def append(self, data):
        """
        Add a data node to the end of the list.
        """
        new_node = _DlNode(data)
        new_node.set_prev(self.__tail)
        if self.__tail is None:
            self.__head = new_node
        else:
            self.__tail.set_next(new_node)
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
            node = node.get_next()
            i += 1
        return node

    def _replace_node_with_node(self, node, new_node):
        if node is None:
            return
        if new_node is None:
            return
        previous = node.get_prev()
        following = node.get_next()
        new_node.set_next(following)
        new_node.set_prev(previous)
        if previous is None:
            self.__head = new_node
        else:
            previous.set_next(new_node)
        if following is None:
            self.__tail = new_node
        else:
            following.set_prev(new_node)

    def _insert(self, idx, data):
        """
        insert an item before the given index.
        - internal implementation
        """
        new_node = _DlNode(data)
        node = self._node_at(idx)
        if node is None:
            return False
        previous = node.get_prev()
        next = node.get_next()
        new_node.set_next(node)
        new_node.set_prev(previous)
        node.set_prev(new_node)
        if previous is None:
            self.__head = new_node
        else:
            previous.set_next(new_node)
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
