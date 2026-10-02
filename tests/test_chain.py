from collectionbox import Chain


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


def test_chain_head_and_tail_getters_return_endpoint_values():
    chain = Chain()
    assert chain.head is None
    assert chain.tail is None

    chain += [1, 2]

    assert chain.head == chain[0]
    assert chain.tail == chain[1]


def test_chain_head_and_tail_setters_replace_endpoint_values():
    chain = Chain()
    chain += [1, 2, 3]

    chain.head = "first"
    chain.tail = "last"

    assert list(chain) == ["first", 2, "last"]
    assert list(reversed(chain)) == ["last", 2, "first"]
    assert len(chain) == 3


def test_chain_endpoint_setters_initialize_an_empty_chain():
    chain = Chain()

    chain.head = "first"
    assert list(chain) == ["first"]
    assert chain.head == "first"
    assert chain.tail == "first"

    chain.clear()
    chain.tail = "last"
    assert list(chain) == ["last"]
    assert chain.head == "last"
    assert chain.tail == "last"


def test_chain_extend():
    c = Chain()

    c.extend([1, 2, 3])
    assert len(c) == 3
    c += [4, 5, 6]
    assert len(c) == 6
    c += 1
    assert list(c) == [1, 2, 3, 4, 5, 6, 1]


def test_chain_iadd_accepts_sequence_protocol_iterables():
    class SequenceProtocol:
        def __getitem__(self, index):
            if index == 0:
                return "first"
            if index == 1:
                return "second"
            raise IndexError

    chain = Chain()
    chain += SequenceProtocol()

    assert list(chain) == ["first", "second"]


def test_chain_extend_with_itself_appends_a_snapshot():
    chain = Chain()
    chain += [1, 2, 3]

    chain.extend(chain)

    assert list(chain) == [1, 2, 3, 1, 2, 3]


def test_chain_iadd_with_itself_appends_a_snapshot():
    chain = Chain()
    chain += [1, 2, 3]

    chain += chain

    assert list(chain) == [1, 2, 3, 1, 2, 3]


def test_chain_combine():
    c1 = Chain()
    c1 += [1, 2, 3]
    c2 = Chain()
    c2 += [4, 5, 6]
    c3 = c1 + c2
    assert len(c3) == 6


def test_chain_copy():
    c1 = Chain()
    c1 += [1, 2, 3]
    c2 = c1.copy()
    assert list(c1) == list(c2)


def test_chain_extend_combine():
    c1 = Chain()
    c1 += [1, 2, 3]
    c2 = Chain()
    c2 += [4, 5, 6]
    c3 = c1 + c2
    c4 = c1.copy()
    c4 += c2
    assert list(c3) == list(c4)
