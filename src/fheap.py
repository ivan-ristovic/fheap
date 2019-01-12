'''
In computer science, a Fibonacci heap is a data structure for priority queue operations, 
consisting of a collection of heap-ordered trees. It has a better amortized running time 
than many other priority queue data structures including the binary heap and binomial heap. 
Michael L. Fredman and Robert E. Tarjan developed Fibonacci heaps in 1984 and published 
them in a scientific journal in 1987. Fibonacci heaps are named after the Fibonacci numbers, 
which are used in their running time analysis.

For the Fibonacci heap, the find-minimum operation takes constant (O(1)) amortized time. The 
insert and decrease key operations also work in constant amortized time. Deleting an element 
(most often used in the special case of deleting the minimum element) works in O(log n) 
amortized time, where n is the size of the heap. This means that starting from an empty data 
structure, any sequence of a insert and decrease key operations and b delete operations would 
take O(a + b log n) worst case time, where n is the maximum heap size. In a binary or binomial 
heap such a sequence of operations would take O((a + b) log n) time. A Fibonacci heap is thus 
better than a binary or binomial heap when b is smaller than a by a non-constant factor. It is 
also possible to merge two Fibonacci heaps in constant amortized time, improving on the 
logarithmic merge time of a binomial heap, and improving on binary heaps which cannot handle 
merges efficiently.

Using Fibonacci heaps for priority queues improves the asymptotic running time of important 
algorithms, such as Dijkstra's algorithm for computing the shortest path between two nodes in 
a graph, compared to the same algorithm using other slower priority queue data structures. 

Source: https://en.wikipedia.org/wiki/Fibonacci_heap
'''

# To allow fast deletion and concatenation, the roots of all trees are linked using a circular, 
# doubly linked list. The children of each node are also linked using such a list. For each node, 
# we maintain its number of children and whether the node is marked. Moreover, we maintain a 
# pointer to the root containing the minimum key.

class FibonacciHeap:

    # Internal Node class.
    class Node:
        def __init__(self, value):
            # We currently only support number elements.
            self.value = value
            # Pointer to the parent node.
            self.parent = None
            # Pointer to the first child in the list of children.
            self.child = None
            # Pointer to the left node.
            self.left = None
            # Pointer to the right node.
            self.right = None
            # Node degree - number of children.
            self.deg = 0
            # Is the node marked? This is needed for some of the operations.
            self.mark = False


    # Pointer to one element of the doubly-linked circular list of heap components.
    root_list =  None
    # Pointer to the node containing minimum element in the heap.
    min_node = None
    # Number of nodes in the entire heap.
    total_num_elements = 0


    # Iterate through the node list
    def iterate(self, head = None):
        if head is None:
            head = self.root_list
        current = head
        while True:
            yield current
            current = current.right
            if current == head:
                break

    # Retrieving minimum node is trivial because we maintain a pointer to it.
    def find_minimum(self):
        if self.min_node is None:
            raise ValueError('Fibonacci heap is empty, minimum does not exist!')
        return self.min_node.value

    # Insert works by creating a new heap with one element and doing merge. This takes constant time, and the potential 
    # increases by one, because the number of trees increases. The amortized cost is thus still constant. 
    def insert(self, value):
        node = self.Node(value)
        node.left = node.right = node
        self.merge_with_root_list(node)
        # update min node
        if self.min_node is not None:
            if self.min_node.value > node.value:
                self.min_node = node
        else:
            self.min_node = node

        self.total_num_elements += 1

    # Extracting minumum element is done in a few steps. First we take the root containing the minimum element and remove 
    # it. Its children will become roots of new trees. If the number of children was d, it takes time O(d) to process all 
    # new roots and the potential increases by d−1. Therefore, the amortized running time of this phase is O(d) = O(log n).
    def extract_minimum(self):
        m = self.min_node
        if m is None:
            raise ValueError('Fibonacci heap is empty, cannot extract mininum!')
        else:
            if m.child is not None:
                # attach children to root_list
                children = [x for x in self.iterate(m.child)]
                for i in range(0, len(children)):
                    self.merge_with_root_list(children[i])
                    children[i].parent = None
                # delete min node
                self.remove_from_root_list(m)
            # update min
            if m == m.right:
                self.min_node = None
                self.root_list = None
            else:
                self.min_node = self.find_min_node_from_scratch()            
            # consolidate trees so that no root has same rank
            self.consolidate()
            
            self.total_num_elements -= 1
        return m.value

    # This operation works by taking the node, decreasing the key and if the heap property becomes violated (the new key 
    # is smaller than the key of the parent), the node is cut from its parent. If the parent is not a root, it is marked. 
    # If it has been marked already, it is cut as well and its parent is marked. We continue upwards until we reach either 
    # the root or an unmarked node. Now we set the minimum pointer to the decreased value if it is the new minimum. In the 
    # process we create some number, say k, of new trees. Each of these new trees except possibly the first one was marked 
    # originally but as a root it will become unmarked. One node can become marked. Therefore, the number of marked nodes 
    # changes by −(k − 1) + 1 = − k + 2. Combining these 2 changes, the potential changes by 2(−k + 2) + k = −k + 4. The 
    # actual time to perform the cutting was O(k), therefore (again with a sufficiently large choice of c) the amortized 
    # running time is constant.
    def decrease_key(self):
        # TODO
        return

    # Delete operation can be implemented simply by decreasing the key of the element to be deleted to minus infinity, thus 
    # turning it into the minimum of the whole heap. Then we call extract minimum to remove it. The amortized running time 
    # of this operation is O(log n).
    def delete(self, key):
        # TODO
        return


    ##### Helper functions #####

    # Merge a node with the doubly linked root list by adding it to second position in the list
    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node

    # Deletes a node from the doubly linked root list.
    def remove_from_root_list(self, node):
        if self.root_list is None:
            raise ValueError('Fibonacci heap is empty, there is no node to remove!')
        if self.root_list == node:
            # check if there's only one element in the list
            if self.root_list == self.root_list.right:
                self.root_list = None
                return
            else:
                self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left
        return
    
    # Consolidates trees so that no root has same rank.
    def consolidate(self):
        ranks_mapping = [None] * self.total_num_elements
        for node in self.iterate(self.root_list):
            degree = node.deg
            while ranks_mapping[degree] != None:
                other = ranks_mapping[degree]
                if node.value < other.value:
                    temp = node
                    node, other = other, temp
                self.merge_heaps(other, node)
                ranks_mapping[degree] = None
                degree += 1
            ranks_mapping[degree] = node

        return

    # Merging two heaps is implemented simply by concatenating the lists of tree roots of the two heaps. 
    # This can be done in constant time and the potential does not change, leading again to constant amortized time.
    def merge_heaps(self, node, other):
        self.remove_from_root_list(other)
        other.left = other.right = other
        # Adding other node to child list of the frst one.
        self.merge_with_child_list(node, other)
        node.deg += 1
        other.parent = node
        other.mark = False

        return

    # Merges a node with the doubly linked child list of the root node.
    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    # Iterates through whole list and finds minimum node.
    def find_min_node_from_scratch(self):
        if self.root_list is None:
            return None
        else:
            min = self.root_list
            for x in self.iterate(self.root_list):
                if x.value < min.value:
                    min = x
            return min

        
    # Prints the whole fheap.
    def print(self, head = None):
        if self.root_list is not None:
            heaps = [x for x in self.iterate()]
            for i in range(0, len(heaps)):
                print('[', end='')
                self.print_tree(heaps[i])
                print(']')
                
    # Prints the node list
    def print_tree(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        if node.child is not None:
            for child in self.iterate(node.child):
                self.print_tree(child)