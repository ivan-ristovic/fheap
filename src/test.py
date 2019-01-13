print("Importing fheap module... ", end='')
from fheap import FibonacciHeap
print("Done.")

print("Beginning tests...")

print("Constructing heap... ", end='')
f = FibonacciHeap()
print("Done.")

print("Inserting elements... ", end='')
f.insert(2)
f.insert(3)
f.insert(4)
f.insert(5)
f.insert(1)
print("Done.")

print("Printing heap...")
f.print()

print("Find min node test:")
print(f.find_min_node().value)

print("Minimum element in heap is: ")
print(f.find_minimum())

print("Minimum element in heap is: ")
print(f.find_min_node().value)

print("Deleting minimum: ")
print(f.extract_minimum())
print("Done!")

print("Printing heap...")
f.print()