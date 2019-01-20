from random import randint
import time
from fheap import FibonacciHeap
from binheap import BinHeap


f = FibonacciHeap()
bh = BinHeap()
n = 1000

print(f"Inserting {n} numbers into heaps... ", end='')
for i in range(0, n):
    r = randint(1, 1000)
    f.insert(r)
    bh.insert(r);
print(f"Done!")

print(f"Running extract_min... ")

#binheap
start_time = time.time()
while bh.current_size > 0:
    bh.extract_minimum()
print(f"\tbinheap: {time.time() - start_time}s")

# fheap
start_time = time.time()
while f.total_num_elements > 0:
    f.extract_minimum()
print(f"\tfheap: {time.time() - start_time}s")

print(f"Done running extract_min banchmark!")


# decrease_key 

f = FibonacciHeap()
bh = BinHeap()
n = 10000

print(f"Inserting {n} numbers into heaps... ", end='')
for i in range(0, n):
    r = randint(1, 1000)
    f.insert(r)
    bh.insert(r);
print(f"Done!")

print(f"Running decrease_key... ")

#binheap
total_time = 0
for i in range(0, bh.current_size - 1):
    max_ind = bh.find_index_of_not(0)
    start_time = time.time()
    bh.decrease_key(max_ind, 0)
    total_time += time.time() - start_time
print(f"\tbinheap: {total_time}s")

# fheap
for i in range(0, f.total_num_elements):
    node_to_decrease = f.find_node_greater_than(0)
    start_time = time.time()
    f.decrease_key(node_to_decrease, 0)
    total_time += time.time() - start_time
print(f"\tfheap: {total_time}s")

print(f"Done running decrease_key banchmark!")