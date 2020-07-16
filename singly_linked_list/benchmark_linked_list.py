import time
from singly_linked_list import LinkedList

n = 100000

l = []
ll = LinkedList()

start_time = time.time()
for i in range(n):
    l.append(i)
end_time = time.time()
print(f"List append took {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    ll.add_to_tail(i)
end_time = time.time()
print(f"Linked List add to tail took {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"Linked List remove from head took {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(f"List pop from took {end_time - start_time} seconds")