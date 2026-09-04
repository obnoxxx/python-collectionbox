#!/usr/bin/env python3

from collectionbox import Set

s = Set()

print(s)

s.add(1)
print(s)
s.add(2)
print(s)
s.remove(1)
print(s)
s.remove(2)
print(s)


s.discard(4)
# s.remove(3)

s2 = Set([1, 2, 3, 4])

print(s2)


A = Set([1, 2, 3])
print("A:", A)
B = Set([2, 3])
print("B:", B)

print("A &B:", A & B)
print("A | B", A | B)
print("A - B:", A - B)
print("B - A:", B - A)
print("A ^B:", A ^ B)
print("B ^A:", B ^ A)
