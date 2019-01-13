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
to_delete = f.insert(4)
to_decrease = f.insert(5)
f.insert(1)
print("Done.")

print("Printing heap...")
f.print()

print("Min: ", end='')
print(f.find_minimum())

print("Min (linear): ", end='')
print(f.find_min_node().value)

print("Deleting minimum: ")
print(f.extract_minimum())
print("Done!")

print("Printing heap...")
f.print()

print("Min: ", end='')
print(f.find_minimum())

print("Min: ", end='')
print(f.find_min_node().value)

print(f"Decrease {to_decrease.value} to 1: ")
f.decrease_key(to_decrease, 1)
f.print()

print("Min: ", end='')
print(f.find_minimum())

print(f"Delete {to_delete.value}: ")
f.delete(to_delete)
f.print()


f2 = FibonacciHeap()
f2.insert(60)
f2.insert(32)

print("Heap 2: ")
f2.print()

print("Merging:")
f.merge(f2)
f.print()