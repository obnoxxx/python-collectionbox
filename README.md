# python collectionbox

## What is collectionbox?

`collectionbox` is a pure-Python library of educational yet production-usable
data structures with clean, Pythonic APIs.

collectionbox currently provides the classes
`Chain`, `Stack`, `Queue`, `SortedChain`, and `Set`.
More details about each class are given below.

This project started as a learning exercise in
object-oriented Python programming and data structures.
It is growing and evolving as additional types are being added.

## Why collectionbox?

Python already provides excellent built-in collection types such as
`list`, `dict`, and `set`. For most applications, these remain the
recommended choice.

collectionbox is not intended to replace Python's native collections.
Instead, it provides a collection framework with a focus on
consistent, uniform, and explicitly object-oriented APIs.
Its goal is to offer consistent interfaces and behavior across different
collection types while
remaining easy to understand, extend, and experiment with.

Unlike wrapper libraries built on top of Python's existing collection
implementations, collectionbox implements its own data structures
from scratch in pure Python.

This makes the project useful as an educational tool and
as a platform for exploring collection abstractions and
object-oriented data-structure design.

collectionbox aims to be both usable and readable.

Because the library is implemented entirely in Python, it may not match
the performance of Python's highly optimized built-in collections.
Performance is therefore not the primary objective. Instead, the focus
is on API consistency, clarity, object-oriented design, and ease of
experimentation.

The project is still evolving. In particular, hash-table and map
(dictionary) types are not yet available.

## What is in the collectionbox?

So far, the package provides five basic collection classes:

- `Chain`, a (doubly) linked list
- `Stack`, a stack implementation (LIFO) based on `Chain`.
- `Queue`, a queue implementation (FIFO) based on `Chain`.
- `SortedChain`, a sorted (doubly) linked list.
- `Set`, an insertion-ordered collection of unique values based on `Chain`.

### Chain

`Chain` is a list-type collection class that is implemented as a
doubly linked list for storing values (data items) of any type.

`Chain()` initializes an empty chain.

`Chain` offers the following methods:

- `append(value)` - add `value` to the end of the chain
- `prepend(value)` - add `value` to the beginning of the chain
- `add(value)` - alias for `append(value)`
- `len()` - return the number of nodes in the chain
- `count(value)` - return the number of nodes with the given value
- `head` - get or set the first value; returns `None` when empty, and setting
  it on an empty chain creates the first node
- `tail` - get or set the last value; returns `None` when empty, and setting
  it on an empty chain creates the first node
- `index(value)` - return the zero-based index of the first matching node, or
  `-1` when absent
- `remove(value)` - remove the first node with the given value, if present
- `remove_all(value)` - remove all nodes with the given value
- `remove_at(index)` - remove the node at the given zero-based index
- `clear()` - remove all nodes

Furthermore, `Chain` supports the following Python collection features:

- `len()` : length
- `repr()` : string representation
- iteration (including reversal)
- truth-value testing

example use:

```python

from collectionbox import Chain
...
lst = Chain()
lst.add(1)
...
```

### Stack

`Stack` implements a stack (LIFO) data structure based on `Chain`.

`Stack()` initializes an empty stack.
Stack supports the following methods:

- `push(item)` - put `item` on top of the stack
- `pop()` - remove and return the top item from the stack
- `peek()` - return the top item without removing it
- `clear()` - remove all items from the stack

Furthermore, `Stack` supports the following Python container features:

- `len()` : length
- `repr()` : string representation
- iteration (including reversal)
- truth-value testing

example use:

```python

from collectionbox import Stack

s = Stack()

s.push(1)
s.push(2)

s.pop()

s.peek()

print(len(s))
print(s)

```

### Queue

`Queue` implements a queue data structure (FIFO) based on `Chain`.

`Queue()` initializes an empty queue.

Queue supports the following methods:

- `enqueue(item)` - add `item` to the end of the queue
- `dequeue()` - remove and return the item at the beginning of the queue
- `clear()` - remove all items from the queue

Furthermore, `Queue` supports these Python container features:

- `len()`: length of the queue
- `repr()`: string representation
- iteration (including reversal)
- truth-value testing

example use:

```python

from collectionbox import Queue

q = Queue()

q.enqueue("John")
q.enqueue("Jane")

print(len(q))
print(q)

q.dequeue()
q.dequeue()

```

### SortedChain

`SortedChain` implements a sorted list as a doubly linked list. Values added
to the collection are kept in ascending order, including duplicate values.

`SortedChain(value)` initializes a chain containing `value` as the only entry.

`SortedChain` offers the following methods:

- `add(value)` - add a value while preserving ascending order
- `remove(value)` - remove the first occurrence of a value
- `remove_all(value)` - remove all occurrences of a value
- `count(value)` - return the number of occurrences of a value
- `index(value)` - return the one-based index of the first occurrence, or `-1`
  when the value is absent
- `lower_bound(value)` - return the one-based index of the first value that is
  greater than or equal to `value`
- `upper_bound(value)` - return the one-based index of the first value that is
  greater than `value`
- `first()` - return the smallest value, or `None` when empty
- `last()` - return the largest value, or `None` when empty
- `clear()` - remove all values

Furthermore, `SortedChain` supports the following features of Python
collections:

- `len()` : length
- `repr()` : string representation
- iteration (including reversal)
- truth-value testing
- one-based indexing
- membership testing

example use:

```python

from collectionbox import SortedChain

chain = SortedChain(5)

for value in [3, 7, 1, 5]:
    chain.add(value)

print(list(chain))  # [1, 3, 5, 5, 7]
print(chain.count(5))  # 2
print(chain.first())  # 1
print(chain.last())  # 7

```

### Set

`Set` stores unique values using a `Chain`. Values retain their insertion
order when iterated, unlike Python's built-in `set`, whose iteration order is
not part of its public contract.

`Set()` initializes an empty set. An optional iterable can be supplied to
initialize it; duplicate values from that iterable are ignored.

`Set` offers the following methods:

- `add(value)` - add `value` when it is not already present
- `remove(value)` - remove `value`, raising `KeyError` when it is absent
- `discard(value)` - remove `value` when present without raising for an absent
  value
- `clear()` - remove all values

`Set` also supports Python container operations for length, representation,
iteration, membership testing, and truth-value testing.

Additionally, `Set` supports the following set operations:

- `union(other)` - form the union with another set
- `intersection(other)` - form the intersection with another set
- `difference(other)` - form the difference with another set
- `symmetric_difference(other)` - form the symmetric difference with another
  set

These operations are also available via corresponding operators:

- `|`
- `&`
- `-`
- `^`

**Limitation:** Because `Set` uses collectionbox's `Chain` as its storage
backend, membership testing has linear time complexity, O(n), in the number of
elements.

Example use:

```python
from collectionbox import Set

values = Set([1, 2, 1])
values.add(3)
values.discard(2)

print(list(values))  # [1, 3]
print(1 in values)  # True

A = Set([1, 2]) # {1, 2}
B = Set([1, 2, 3]) # {1, 2, 3}
C = A|B # union: {1, 2}
D = A&B # intersection: {1, 2}
E = A - B # difference: {}
F = B - A # difference: { 3}

```

## Where can I get collectionbox?

collectionbox requires Python 3.9 or later and is available from
[PyPI](https://pypi.org/project/collectionbox/).

You can install and play with it like this:

```console
$ python3 -m pip install collectionbox
$ python3
>>> from collectionbox import Set
>>> values = Set([1, 2, 1])
>>> values.add(3)
>>> values
{1, 2, 3}
>>> list(values)
[1, 2, 3]
>>>
```
