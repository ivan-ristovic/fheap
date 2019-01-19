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
    bh.insert(n);
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