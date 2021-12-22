class MinHeap:
    """
    A variable arity minimum heap.
    """
    def __init__(self, arr = [], d = 2):
        """
        Initializes a d-ary minheap.

        Params:
            arr : [Orderable] - Optional starting array.
            d : int - Arity of the heap.

        Returns:
            Heap - The Heap object.
        """
        self._d = d
        self._arr = arr.copy()
        
        if self._arr:
            self.heapify()

    def heapify(self):
        """
        Heapifies the internal array.
        """
        for i in reversed(range((len(self._arr) + 1) // self._d + 1)):
            self._move_down(i)

    def insert(self, elem):
        """
        Inserts an element into the heap, preserving minheap properties.

        Params:
            elem : Orderable - The element to insert.
        """
        self._arr.append(elem)
        self._move_up(len(self._arr) - 1)

    def peek_min(self):
        """
        Returns the smallest element in the heap without removal.

        Returns:
            Orderable - The smallest element in the heap.
        """
        if not self._arr:
            raise IndexError("Heap is empty.")
        return self._arr[0]

    def extract_min(self):
        """
        Removes and returns the smallest element in the heap.

        Returns:
            Orderable - The smallest element in the heap.
        """
        if not self._arr:
            raise IndexError("Heap is empty.")
        self._swap(0, len(self._arr) - 1)
        min_elem = self._arr.pop()
        self._move_down(0)
        return min_elem

    def is_empty(self):
        """
        Checks if the heap is empty.

        Returns:
            boolean - True if the heap is empty, False otherwise.
        """
        return self.size() == 0

    def size(self):
        """
        Gets the size of the heap.

        Returns:
            int - The size of the hepa.
        """
        return len(self._arr)

    def _move_down(self, idx):
        """
        Moves down a node at the given index, preserving minheap properties.

        Params:
            idx : int - Index to move down.
        """
        try:
            min_child = self._get_min_child(idx)
            if self._arr[idx] > self._arr[min_child]:
                self._swap(idx, min_child)
                self._move_down(min_child)
        except ValueError:
            return

    def _move_up(self, idx):
        """
        Moves up a node at the given index, preserving minheap properties.(minheap.extract_min()

        Params:
            idx : int - Index to move up.
        """
        try:
            parent = self._get_parent(idx)
            if self._arr[idx] < self._arr[parent]:
                self._swap(idx, parent)
                self._move_up(parent)
        except ValueError:
            return

    def _get_children(self, idx):
        """
        Gets the indices of all children of a parent index.

        Params:
            idx : int - The parent index.

        Returns:
            [int] - List of children indices.
        """
        first_child = idx * self._d + 1
        return list(filter(lambda i : i < len(self._arr), [first_child + i for i in range(self._d)]))

    def _get_parent(self, idx):
        """
        Gets the parent index of a given child index.

        Params:
            idx : int - The child index.

        Returns:
            int - The parent index.
        """
        if idx < 0:
            raise ValueError("No parent index.")
        return (idx - 1) // self._d

    def _get_min_child(self, idx):
        """
        Gets the index of the minimum child of a parent node.

        Params:
            idx : int - The parent index.

        Returns:
            int - The minimum child index.
        """
        try:
            return min(self._get_children(idx), key=lambda i : self._arr[i])
        except ValueError:
            raise ValueError("No children.")

    def _swap(self, i, j):
        """
        Swaps the positions of two elements in the heap.

        Params:
            i : int - The index of the first element.
            j : int - The index of the second element.
        """
        tmp = self._arr[i]
        self._arr[i] = self._arr[j]
        self._arr[j] = tmp
