from containerbox import Chain


class Queue:
    def __init__(self):
        self._chain = Chain()

    def enqueue(self, item):
        self._chain.append(item)

    def dequeue(self):
        val = self._chain[0]
        self._chain.remove_at(0)
        return val

    def __len__(self):
        return len(self._chain)

    def __repr__(self):
        return f"Queue({list(self._chain)})"

    def __bool__(self):
        return len(self) > 0

    def __iter__(self):
        return iter(self._chain)

    def __reversed__(self):
        return reversed(self._chain)

    def clear(self):
        self._chain.clear()
