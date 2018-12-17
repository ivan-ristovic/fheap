# Comments: https://en.wikipedia.org/wiki/Fibonacci_heap
# To allow fast deletion and concatenation, the roots of all trees are linked using a circular, doubly linked list. The children of each node are also linked using such a list. For each node, we maintain its number of children and whether the node is marked. Moreover, we maintain a pointer to the root containing the minimum key.

# TODO about fheap
class FibonacciHeap:

	# pointer to one element of the circular list of root nodes of sub-heaps
	root_list =  None
	# pointer to the node containing minimum element in the heap
	min_node = None
	# number of elements in the Fibonacci heap
	total_num_elements = 0

    class Node:
        def __init__(self, value):
			# We currently only support number elements
            self.value = value
			# Pointer to the parent node
            self.parent = None
			# Pointer to the first child in the list of children
			self.child = None
			# Pointer to the left node
			self.left = None
			# Pointer to the right node
			self.right = None
			# Node degree - number of children
            self.deg = 0
			# Is node marked? This is needed for some of the operations.
            self.mark = False

	# O(1)
    def find_minimum():
		if min_node == None:
			raise ValueError('Fibonacci heap is empty!')
		return min_node.value

	def merge():
		# TODO
		#is implemented simply by concatenating the lists of tree roots of the two heaps. This can be done in constant time and the potential does not change, leading again to constant amortized time.
		
	def insert():
		# TODO
		#works by creating a new heap with one element and doing merge. This takes constant time, and the potential increases by one, because the number of trees increases. The amortized cost is thus still constant.

	def extract_minimum():
		# TODO
		# First we take the root containing the minimum element and remove it. Its children will become roots of new trees. If the number of children was d, it takes time O(d) to process all new roots and the potential increases by d−1. Therefore, the amortized running time of this phase is O(d) = O(log n).
		
	def decrease_key():
		# TODO
		#will take the node, decrease the key and if the heap property becomes violated (the new key is smaller than the key of the parent), the node is cut from its parent. If the parent is not a root, it is marked. If it has been marked already, it is cut as well and its parent is marked. We continue upwards until we reach either the root or an unmarked node. Now we set the minimum pointer to the decreased value if it is the new minimum. In the process we create some number, say k, of new trees. Each of these new trees except possibly the first one was marked originally but as a root it will become unmarked. One node can become marked. Therefore, the number of marked nodes changes by −(k − 1) + 1 = − k + 2. Combining these 2 changes, the potential changes by 2(−k + 2) + k = −k + 4. The actual time to perform the cutting was O(k), therefore (again with a sufficiently large choice of c) the amortized running time is constant.

	def delete():
		# TODO
		#can be implemented simply by decreasing the key of the element to be deleted to minus infinity, thus turning it into the minimum of the whole heap. Then we call extract minimum to remove it. The amortized running time of this operation is O(log n).

		