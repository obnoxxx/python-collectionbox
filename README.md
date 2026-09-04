# python collectionbox

The collectionbox package is a pure-Python collection of educational yet production-usable
collection data structures with clean, pythonic APIs.

This project started as a learning exercise in
object oriented python programming and data structure types.
It is growing and evolving as additional types are being added.

So far, the package provides five basic collection classes:

- `Chain`, a (doubly) linked list
- `Stack`- a stack implementation (LIFO) based on `Chain`.
- `Queue`- a queue implementation (FIFO)based on `Chain`.
- `SortedChain`, a sorted (doubly) linked list.
- `Set`, an insertion-ordered collection of unique values based on `Chain`.

## Chain

`Chain` is a list-type collection class that is implemented as a
doubly linked list for storing values (data items) of any type.

`Chain()` initializes an empty chain that can be added to.

`Chain` offers the following methods:

- `append(value)` - add to the end of the  list
- `prepend(value)` - add to the beginning of the list
- `add(value)` - alias for append
- `len()` - number of nudes in the list
- `count(value)` - return number of nodes with given value
- `get_head()` - return the value of first node
- `get_tail()` - return the value of last node
- `index(value)`- return the index of first node with the given value
- `remove(value)` - remove the first node with the given value
- `remove_all(value)` - remove all nodes with the given value
- `insert(index, value)` - insert a node with the given value right before
  the given index
- `clear()` - drain the list, i. e. remove all nodes

Furthermore, Chain supports the following features of python collections:

- len : length
- repr : string representation
- iteration (including reversal)
- bool : check if empty

example use:

```python

from collectionbox import Chain
...
lst = Chain()
lst.add(1)
...
```

## Stack

`Stack` implements a stack (LIFO) data structure based on `Chain`.

`Stack()`initializes an empty stack.
Stack supports the following methods:

- `push(data) - put a leaf with given dta  on top of the stack
- `pop()` - remove the top leaf from the stack, returning its data
- `peek()`- the leaf's data without removing it.
- `clear()` - remove all leaves from the stack

Furthermore, `Stack` supports the following features of python containers:

- len : length
- repr : string representation
- iteration (including reversal)
- bool : check if empty

example use:

```python

from collectionbox import Stack

s = Stack()

s.push(1)
s.push(2)

s.pop()

s.peek()

print(len(s)
print(s)

```

## Queue

`Queue` implements a queue data structure (FIFO) based on `Chain`.

`Queue()` initializes an empty queue.

Queue supports the following methods:

- `enqueue(data)` - add to the end of the queue
- `dequeue()`- remove from beginning of the queue
- `clear()` - drain the queue, removong all entries

Furthermore, `Queue` supports these features of python containers:

- len: length of the queue
- repr: string representation
- iteration (including reversal)
- bool : check if empty

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

## SortedChain

`SortedChain` implements a sorted list as a doubly linked list. Values added
to the collection are kept in ascending order, including duplicate values.

`SortedChain(value)` initializes a chain containing `value` as the only enrty

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

- len : length
- repr : string representation
- iteration (including reversal)
- bool : check if empty
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

## Set

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
iteration, and membership testing.

Limitation:

Note that, due to the use of collectionbox's `Chain` as a storage backend,
element lookup in `Set` has linear complexity, O(n), in the number of elements.

Limitation:

Note that, due to the use of colectionbox's  Chain as a storage backend,
elemen lookup in Set is of lineat complexity O(n) in the number of elements.

Example use:

```python
from collectionbox import Set

values = Set([1, 2, 1])
values.add(3)
values.discard(2)

print(list(values))  # [1, 3]
print(1 in values)  # True
```
