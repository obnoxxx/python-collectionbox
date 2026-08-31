# python collectionbox

The collectionbox package is a pure-Python collection of educational yet production-usable
collection data structures with clean, pythonic APIs.

This project started as a learning exercise in
object oriented python programming and data structure types.
It is growing and evolving as additional types are being added.

So far, the package provides three basic collection classes:

- `Chain`, a (doubly) linked list
- `Stack`- a stack implementation (LIFO) based on `Chain`.
- `Queue`- a queue implementation (FIFO)based on `Chain`.

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
