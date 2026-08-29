"""
This is the sortedchain/SortedChain module/class of the collectionbox package
It implements a sorted (doubly) linked list class SortedChain using an internal node class _ScNode
"""

import math

"""
_Node is the internal node representation for the sorted list class SortedChain
and the corresponding block class _Block.
_ScNode is intentiopnally kept minimal and dumb:
All modifying operations are performed by the SortedChain class.

"""


class _Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


"""
_Block is the internal representation of a block of nodes.
It decomposes the list Class SortedChain into blocks of nodes.
A block is itself a small list.
The (Sc)Block class is intentioally kept minimal and dumb:
    All modifying operations are done from the SortedChain class.
"""


class _Block:
    __slots__ = ("head", "tail", "size", "next_block", "prev_block")

    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size
        self.next_block = None
        self.prev_block = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            if current is self.tail:
                break
            current = current.next


"""
Ste SortedChain class implements a sorted list as a doubly linked list with
jump search/block decomposition for time fficiency.
Block length is chosen as sqrt(len).
"""


class SortedChain:

    def __init__(self, value):
        node = _Node(value)
        block = _Block(node, node, 1)
        self.__head_node = node
        self.__tail_node = node
        self.__size = 1
        self.__head_block = block
        self.__tail_block = block
        self.__block_size_limit = 2

    def link_nodes(self, prev, new, next):
        new.prev = prev
        new.next = next
        if prev is not None:
            prev.next = new
        if next is not None:
            next.prev = new

    def block_bounds(self, block):
        return block.head.value, block.tail.value

    def insert_into_block(self, block, value):
        pos = self.scan_block(block, value)
        new = _Node(value)
        if pos is None:
            self.link_nodes(block.tail, new, None)
            block.tail = new
            if block is self.__tail_block:
                self.__tail_node = new
        else:
            self.link_nodes(pos.prev, new, pos)
            if pos is block.head:
                block.head = new
                if block is self.__head_block:
                    self.__head_node = new

        block.size += 1
        self.__size += 1
        self._update_block_size_limit()

        if block.size > self.__block_size_limit:
            self.split_block(block)

    def jump_search(self, value):
        """Return the first block whose maximum is at least ``value``."""
        block = self.__head_block
        while block is not None and block.tail.value < value:
            block = block.next_block
        return block or self.__tail_block

    def scan_block(self, block, value):
        """Return the first node in ``block`` whose value is at least ``value``."""
        current = block.head
        while current is not None:
            if current.value >= value:
                return current
            if current is block.tail:
                return None
            current = current.next
        return None

    def find(self, value):
        """Return the first matching node, or ``None`` when absent."""
        block = self.jump_search(value)
        if block is None:
            return None
        node = self.scan_block(block, value)
        return node if node and node.value == value else None

    def link_blocks(self, prev, new, next):
        new.prev_block = prev
        new.next_block = next
        if prev is not None:
            prev.next_block = new
        else:
            self.__head_block = new
        if next is not None:
            next.prev_block = new
        else:
            self.__tail_block = new

    def set_block_bounds(self, block, head, tail, size):
        block.head = head
        block.tail = tail
        block.size = size

    def split_block(self, block):
        original_size = block.size
        mid = original_size // 2
        cur = block.head
        for _ in range(mid):
            cur = cur.next

        new_block = _Block()

        old_tail = block.tail
        new_head = cur

        prev = cur.prev
        prev.next = None
        cur.prev = None

        self.set_block_bounds(block, block.head, prev, mid)
        self.set_block_bounds(new_block, new_head, old_tail, original_size - mid)

        self.link_blocks(block, new_block, block.next_block)

    def _update_block_size_limit(self):
        self.__block_size_limit = max(2, math.ceil(math.sqrt(self.__size)))

    def _merge_blocks(self, first, second):
        first.tail.next = second.head
        second.head.prev = first.tail
        first.tail = second.tail
        first.size += second.size
        self._remove_block(second)

    def _rebalance_blocks(self):
        block = self.__head_block
        while block is not None:
            if block.size > self.__block_size_limit:
                self.split_block(block)
                continue
            following = block.next_block
            if (
                following is not None
                and block.size + following.size <= self.__block_size_limit
            ):
                self._merge_blocks(block, following)
                continue
            block = following

    def __len__(self):
        return self.__size

    def __bool__(self):
        return len(self) > 0

    def __repr__(self):
        return f"SortedChain({list(self)})"

    def _index_is_in_bounds(self, idx):
        return 1 <= idx <= self.__size

    def _get_node(self, idx):
        if not self._index_is_in_bounds(idx):
            raise IndexError("list index out of range")
        idx -= 1
        block = self.__head_block
        while idx >= block.size:
            idx -= block.size
            block = block.next_block
        node = block.head
        for _ in range(idx):
            node = node.next
        return node

    def __getitem__(self, idx):
        return self._get_node(idx).value

    def __iter__(self):
        block = self.__head_block
        while block is not None:
            for node in block:
                yield node.value
            block = block.next_block

    def __reversed__(self):
        block = self.__tail_block
        while block is not None:
            current = block.tail
            while current is not None:
                yield current.value
                if current is block.head:
                    break
                current = current.prev
            block = block.prev_block

    def __contains__(self, value):
        return self.find(value) is not None

    def add(self, value):
        """Add ``value`` while preserving ascending order."""
        if not self:
            node = _Node(value)
            block = _Block(node, node, 1)
            self.__head_node = self.__tail_node = node
            self.__head_block = self.__tail_block = block
            self.__size = 1
            self._update_block_size_limit()
            return
        self.insert_into_block(self.jump_search(value), value)

    def remove(self, value):
        """Remove the first node containing ``value`` if it is present."""
        node = self.find(value)
        if node is None:
            return
        block = self.jump_search(value)
        previous, following = node.prev, node.next
        if node is block.head:
            block.head = following
        else:
            previous.next = following
        if node is block.tail:
            block.tail = previous
        else:
            following.prev = previous

        block.size -= 1
        self.__size -= 1
        if block.size == 0:
            self._remove_block(block)
        if self.__size == 0:
            self.__head_node = self.__tail_node = None
        else:
            self._update_block_size_limit()
            self._rebalance_blocks()
            self.__head_node = self.__head_block.head
            self.__tail_node = self.__tail_block.tail
            return
        self._update_block_size_limit()

    def _remove_block(self, block):
        previous, following = block.prev_block, block.next_block
        if previous is not None:
            previous.next_block = following
        else:
            self.__head_block = following
        if following is not None:
            following.prev_block = previous
        else:
            self.__tail_block = previous

    def remove_all(self, value):
        """Remove every node containing ``value``."""
        while value in self:
            self.remove(value)

    def index(self, value):
        """Return the first index of ``value``, or ``-1`` if it is absent."""
        index = self.lower_bound(value)
        return index if index <= self.__size and self[index] == value else -1

    def lower_bound(self, value):
        """Return the first index containing a value greater than or equal to ``value``."""
        index = 1
        block = self.__head_block
        while block is not None:
            if block.tail.value < value:
                index += block.size
                block = block.next_block
                continue
            node = block.head
            while node is not None and node.value < value:
                index += 1
                if node is block.tail:
                    break
                node = node.next
            return index
        return index

    def upper_bound(self, value):
        """Return the first index containing a value greater than ``value``."""
        index = 1
        block = self.__head_block
        while block is not None:
            if block.tail.value <= value:
                index += block.size
                block = block.next_block
                continue
            node = block.head
            while node is not None and node.value <= value:
                index += 1
                if node is block.tail:
                    break
                node = node.next
            return index
        return index

    def count(self, value):
        """ "return the numb=er of occurrences of ```value```"""
        if self.find(value) is None:
            return 0
        return self.upper_bound(value) - self.lower_bound(value)

    def first(self):
        """Return the first (smallest) value, or ``None`` when empty."""
        return None if self.__head_node is None else self.__head_node.value

    def last(self):
        """Return the last (largest) value, or ``None`` when empty."""
        return None if self.__tail_node is None else self.__tail_node.value

    def clear(self):
        """Drain the entire list."""
        self.__head_node = None
        self.__tail_node = None
        self.__head_block = None
        self.__tail_block = None
        self.__size = 0
        self._update_block_size_limit()
