#!/usr/bin/env python3

from collectionbox import SortedChain

chain = SortedChain(5)

print(" initial chain:", list(chain))
print("index of 5:", chain.index(5))
print("bounds for 5:", chain.lower_bound(5), chain.upper_bound(5))
chain.add(6)
print("chain after adding 6:", list(chain))
print("index of 5:", chain.index(5))
print("bounds for 5:", chain.lower_bound(5), chain.upper_bound(5))
print("index of 6:", chain.index(6))
print("bounds for 6:", chain.lower_bound(6), chain.upper_bound(6))
chain.add(5)
print("chain after adding 5:", list(chain))
print("index of 5:", chain.index(5))
print("bounds for 5:", chain.lower_bound(5), chain.upper_bound(5))
print("index of 6:", chain.index(6))
print("bounds for 6:", chain.lower_bound(6), chain.upper_bound(6))
print("adding 6...")
chain.add(6)
print("chain after adding 6:", list(chain))
print("index of 6:", chain.index(6))
print("bounds for 6:", chain.lower_bound(6), chain.upper_bound(6))
print("adding 6...")
chain.add(6)
print("chain after adding 6:", list(chain))
print("index of 6:", chain.index(6))
print("bounds for 6:", chain.lower_bound(6), chain.upper_bound(6))

for value in [3, 7, 1, 9, 5, 4, 8, 2, 6, 0]:
    chain.add(value)

print("sorted:", list(chain))
for i in range(1, len(chain) + 1):
    print(i, ":", chain[i])
print("reversed:", list(reversed(chain)))
print("first:", chain.first())
print("last:", chain.last())
print("index of 5:", chain.index(5))
print("bounds for 5:", chain.lower_bound(5), chain.upper_bound(5))

chain.remove(5)
chain.remove_all(3)
print("after removals:", list(chain))
