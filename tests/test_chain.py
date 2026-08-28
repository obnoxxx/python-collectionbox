from containerbox import Chain


def test_chain():
    lst = Chain()
    assert len(lst) == 0
    lst.add(1)
    assert len(lst) == 1
    assert lst[0] == 1
    lst.add(2)
    assert len(lst) == 2
    assert lst[1] == 2
    lst += [3, 4, 5]
    assert len(lst) == 5
    assert lst[2] == 3
    # corner case of nonexisting value
    assert lst.index(10) == -1
    lst.clear()
    assert len(lst) == 0


def test_chain_iteration_starts_at_the_head():
    chain = Chain()
    chain.add("first")
    chain.add("second")
    chain.add("third")

    assert list(chain) == ["first", "second", "third"]


def test_chain_reverse_iteration_starts_at_the_tail():
    chain = Chain()
    chain.add("first")
    chain.add("second")
    chain.add("third")

    assert list(reversed(chain)) == ["third", "second", "first"]
