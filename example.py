from fheap import FibonacciHeap
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