from heapq import *
from random import randint
import time
from fheap import FibonacciHeap


f = FibonacciHeap()
h = []
n = 100
for i in range(0, n):
    r = randint(1, 1000)
    f.insert(r)
    heappush(h, r)


# heapq
start_time = time.time()
while h:
    heappop(h)
print(f"heapq: {time.time() - start_time}s")

# fheap 
start_time = time.time()
while f.total_num_elements > 0:
    f.extract_minimum()
print(f"fheap: {time.time() - start_time}s")