#!/usr/bin/env python3
from containerbox import Stack

s = Stack()
print("length of new stack:", len(s))

s.push(1)
print("pushed", s.peek())
s.push(2)
print("pushed", s.peek())
print("length after two pushes:", len(s))
print("stack now looks like this:", s)
print("stack dump:")
for leaf in s:
    print("leaf:", leaf)
print("reverse stack dump:")
for leaf in reversed(s):
    print("leaf:", leaf)
print("pop from top:", s.pop())
print("length after pop:", len(s))
print("peek top(without pop):", s.peek())
print("pop again:", s.pop())
print("length now:", len(s))
