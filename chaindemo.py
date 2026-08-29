#!/usr/bin/env python3

from collectionbox import Chain

mylist = Chain()


print("len of new list:", mylist.len())

mylist.append(1)

print("len after append:", mylist.len())

mylist.prepend(1)
mylist.append(2)

print("len after prepend and append:", mylist.len())


print("position of first node with 1:", mylist.index(1))
print("number of 1's in the list", mylist.count(1))

mylist.remove_all(1)

mylist.prepend(1)
mylist.append(1)

print("len after removing all nodes with 1:", mylist.len())


print("all items in list:")

num = 0
for item in mylist:
    num += 1
    print("item number ", num, ":", item)
