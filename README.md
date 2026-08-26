# python containerbox

A python package with various container data structures.

This project started as a learning exercise in
object oriented python programming and data structure types.

So far, the package provides one class: `Chain`.

## Chain

Chain is a list-type container class that is implemented as a
doubly linked list for storing values (data items) of any type.

```python

from containerbox import Chain
...
lst = Chain()
lst.add(1)
...
```

`Chain()` will initialize an empty chain that can be added to.

`Chain offers the following methods:

- `append(value)` - add to the end of the  list
- `prepend(value)` - add to the beginning of the list
- `add(value)` - alias for append
- `len()` - number of nudes in the list
- `count(value)` - return number of nodes with given value
- `get_head()` - return the value of first node
- `get_tail()` - return the value of last node
- `index(value)`- return the index of first node with the given value
- `remove(value)` - remove the first node with the given value
- `remove_all(value)` - remove allnodes with the given value
- `insert(index, value)` - insert a node with the given value right before
  the given index
