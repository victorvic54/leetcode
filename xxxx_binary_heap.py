class BinaryHeap:
    def __init__(self, heap):
        self.heap = []

    def heapify(self, elems):
        for elem in elems:
            self.heap.append(elem)

        # important, need to go from lower node to root node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.sink(i)

    def is_empty(self):
        return len(self.heap) == 0

    def clear(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

    def poll(self):
        return self.removeAt(0)

    def contains(self, elem):
        for val in self.heap:
            if elem == val:
                return True
        return False

    def add(self, elem):
        self.heap.append(elem)
        self.swim(len(self.heap) - 1)

    def less(self, i, j):
        return self.heap[i] <= self.heap[j]

    # Perform bottom up node swim, O(log(n))
    def swim(self, k):
        parent = (k - 1) // 2

        while parent >= 0 and self.less(k, parent):
            self.swap(k, parent)

            k = parent
            parent = (k - 1) // 2


    # Top down node sink, O(log(n))
    def sink(self, k):
        while True:
            left_idx = 2 * k + 1
            right_idx = 2 * k + 2
            smallest = left_idx

            if right_idx < len(self.heap) and self.less(right_idx, left_idx):
                smallest = right_idx

            if left_idx >= len(self.heap) or self.less(k, smallest):
                break

            self.swap(smallest, k)
            k = smallest

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def remove(self, elem):
        for i in range(len(self.heap)):
            if self.heap[i] == elem:
                self.removeAt(i)
                return True
        return False

    # Removes a node at particular index, O(log(n))
    def removeAt(self, i):
        if self.heap == []:
            return None

        poll_val = self.heap[i]
        new_val = self.heap[-1]

        self.swap(i, len(self.heap) - 1)
        self.heap.pop()

        self.sink(i)
        if self.heap[i] == new_val:
            self.swim(i)

        return poll_val

    """
    Recursively checks if this heap is a min heap
    This method is just for testing purposes to make
    sure the heap invariant is still being maintained
    Called this method with k=0 to start at the root
    """
    def isMinHeap(self, k):
        if k >= len(self.heap):
            return True

        left_idx = 2 * k + 1
        right_idx = 2 * k + 2

        if left_idx < len(self.heap) and not self.less(k, left_idx):
            return False

        if right_idx < len(self.heap) and not self.less(k, right_idx):
            return False
        
        return self.isMinHeap(left_idx) and self.isMinHeap(right_idx)
