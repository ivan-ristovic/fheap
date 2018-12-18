print("Importing fheap module... ", end='')
from fheap import FibonacciHeap
print("Done.")

print("Beginning tests...")

print("Constructing heap... ", end='')
f = FibonacciHeap()
print("Done.")

print("Inserting elements... ", end='')
f.insert(1)
f.insert(2)
f.insert(3)
f.insert(4)
f.insert(5)
print("Done.")

print("Printing heap...")
f.print()
