from containerbox import Stack


def test_stack():
    stack = Stack()

    assert len(stack) == 0

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert len(stack) == 3
    assert stack.peek() == 3
    assert len(stack) == 3

    assert repr(stack) == "Stack([3, 2, 1])"

    assert stack.pop() == 3
    assert repr(stack) == "Stack([2, 1])"
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert len(stack) == 0
    stack.clear()
    assert not stack


def test_stack_iteration_starts_at_the_top():
    stack = Stack()
    stack.push("first")
    stack.push("second")
    stack.push("third")

    assert list(stack) == ["third", "second", "first"]


def test_stack_reverse_iteration_starts_at_the_bottom():
    stack = Stack()
    stack.push("first")
    stack.push("second")
    stack.push("third")

    assert list(reversed(stack)) == ["first", "second", "third"]
