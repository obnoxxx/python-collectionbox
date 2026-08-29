from collectionbox import Queue


def test_queue():
    q = Queue()
    assert len(q) == 0
    q.enqueue("a")
    assert len(q) == 1
    q.enqueue("b")
    assert len(q) == 2
    assert repr(q) == "Queue(['a', 'b'])"
    q.dequeue()
    assert len(q) == 1
    assert repr(q) == "Queue(['b'])"
    q.enqueue("c")
    assert len(q) == 2
    assert repr(q) == "Queue(['b', 'c'])"
    q.dequeue()
    assert len(q) == 1
    q.dequeue()
    assert len(q) == 0
    assert not q
    q.enqueue("a")
    assert len(q) == 1
    q.clear()
    assert not q


def test_queue_iteration_starts_at_the_front():
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    assert list(queue) == ["first", "second", "third"]


def test_queue_reverse_iteration_starts_at_the_back():
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    assert list(reversed(queue)) == ["third", "second", "first"]
