# fheap
Fibonacci Heap implementation in Python for the course: Algorithms Construction and Analysis 2. 

The paper we wrote (in Serbian) can be read ![here](paper/fheap.pdf).


## About Fibonacci heaps

> In computer science, a Fibonacci heap is a data structure for priority queue operations, 
consisting of a collection of heap-ordered trees. It has a better amortized running time 
than many other priority queue data structures including the binary heap and binomial heap. 
Michael L. Fredman and Robert E. Tarjan developed Fibonacci heaps in 1984 and published 
them in a scientific journal in 1987. Fibonacci heaps are named after the Fibonacci numbers, 
which are used in their running time analysis. Using Fibonacci heaps for priority queues 
improves the asymptotic running time of important algorithms, such as Dijkstra's algorithm 
for computing the shortest path between two nodes in a graph, compared to the same algorithm 
using other slower priority queue data structures. 
Source: ![Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_heap)

More information can be obtained from the original 
![paper](http://www.cs.cmu.edu/~sleator/papers/pairing-heaps.pdf) or from the 
following ![slides](https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf).

### Complexity comparison (theoretical)

| **Operation** | **Binary heap** | **Fibonacci heap** |
| :--- | :--- | :--- |
| `find_min()` | O(1) | O(1) |
| `extract_min()` | O(log n) | O(log n) |
| `insert(v)` | O(log n) | O(1) |
| `decrease_key(k, v)` | O(log n) | O(1) |
| `merge(h)` | O(n) | O(1) |


## Usage

See the ![test file](fheap_test.py) for more detailed examples.

```python
f = FibonacciHeap()

f.insert(10)
f.insert(2)
f.insert(50)
f.insert(5)

f.print()

print(f.extract_minimum())

print(f.find_minimum())

f2 = FibonacciHeap()
f2.insert(12)
f2.insert(222)
f2.insert(54)

f.merge(f2)
f.print()

f.decrease_key(f.root_list.right.right, 1)
f.print()

f.delete(f.root_list.right)
f.print()
```

## Performance comparison

*TODO*