# Class that represents binary min heap.

class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0


    def cascade_up(self,i):
        while i // 2 > 0:
          if self.heap_list[i] < self.heap_list[i // 2]:
             tmp = self.heap_list[i // 2]
             self.heap_list[i // 2] = self.heap_list[i]
             self.heap_list[i] = tmp
          i = i // 2

    def insert(self, k):
      self.heap_list.append(k)
      self.current_size = self.current_size + 1
      self.cascade_up(self.current_size)

    def cascade_down(self, i):
      while (i * 2) <= self.current_size:
          mc = self.min_child(i)
          if self.heap_list[i] > self.heap_list[mc]:
              tmp = self.heap_list[i]
              self.heap_list[i] = self.heap_list[mc]
              self.heap_list[mc] = tmp
          i = mc

    def min_child(self, i):
      if i * 2 + 1 > self.current_size:
          return i * 2
      else:
          if self.heap_list[i*2] < self.heap_list[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def extract_minimum(self):
      retval = self.heap_list[1]
      self.heap_list[1] = self.heap_list[self.current_size]
      self.current_size = self.current_size - 1
      self.heap_list.pop()
      self.cascade_down(1)
      return retval

    def decrease_key(self, i, value):
        if value > self.heap_list[i]:
            raise ValueError("Cannot decrease key with a value greater than what it already is.")
        self.heap_list[i] = value
        self.cascade_up(i)

    def build_heap(self, alist):
      i = len(alist) // 2
      self.current_size = len(alist)
      self.heap_list = [0] + alist[:]
      while (i > 0):
          self.cascade_down(i)
          i = i - 1

    def find_index_of_not(self, value):
        for i in range(0, self.current_size - 1):
            if self.heap_list[self.current_size - i] != value:
                return self.current_size - i
        raise ValueError(f"Cannot find an element that is not {value}.")