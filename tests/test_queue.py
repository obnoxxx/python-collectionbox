from containerbox import Queue


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
