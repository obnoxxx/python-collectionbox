"""
Internal node representation for the doubly linked lis class (DlList).
Hidden from list consumers.
"""


class _DlNode:
    def __init__(self, data, _prev=None, _next=None):
        """
        By defaukt, sart with a node that is not connected
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
