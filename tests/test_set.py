import pytest

from collectionbox import Set


def test_set_adds_unique_values_and_iterates_in_insertion_order():
    values = Set([1, 2, 1])
    values.add(3)
    values.add(2)

    assert list(values) == [1, 2, 3]
    assert len(values) == 3
    assert 2 in values
    assert 4 not in values


def test_set_repr_uses_set_syntax():
    assert repr(Set()) == "{}"
    assert repr(Set([1, 2, 3, 4])) == "{1, 2, 3, 4}"
    assert repr(Set(["one", "two"])) == "{'one', 'two'}"


def test_set_remove_discard_and_clear():
    values = Set([1, 2])

    values.remove(1)
    values.discard(3)

    assert list(values) == [2]
    with pytest.raises(KeyError):
        values.remove(3)

    values.clear()
    assert len(values) == 0
