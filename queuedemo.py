#!/usr/bin/env python3
from collectionbox import Queue

q = Queue()

print("started queue (empty)")
print("The queue:", q)

q.enqueue("Bob")
print("Bob has enqueued.")
print("The queue:", q)
q.enqueue("Tony")
print("Tony has enqueued.")
print("The queue:", q)
q.enqueue("Mary")
print("Mary has enqueued.")
print("The queue:", q)
print("queue traversal:")
for item in q:
    print("item:", item)
print("reverse queue traversal:")
for item in reversed(q):
    print("item:", item)

q.dequeue()
print("The queue after dequeue:", q)
q.dequeue()
print("The queue after dequeue:", q)
q.dequeue()
print("The queue after dequeue:", q)
