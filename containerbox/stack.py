from containerbox import Chain


class Stack:
    def __init__(self):
        self._chain = Chain()

    def push(self, item):
        self._chain.prepend(item)

    def pop(self):
        val = self._chain[0]
        self._chain.remove_at(0)
        return val

    def __len__(self):
        return len(self._chain)

    def __bool__(self):
        return len(self) > 0

    def peek(self):
        return self._chain[0]

    def __repr__(self):
        return f"Stack({list(self._chain)})"
