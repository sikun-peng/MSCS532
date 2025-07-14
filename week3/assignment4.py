# -------------------- Heapsort Implementation --------------------

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
    return arr

# -------------------- Priority Queue with Heap --------------------

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task({self.task_id}, Priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        max_task = self.heap.pop()
        self._heapify(0)
        return max_task

    def increase_key(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority
                    self._sift_up(i)
                return

    def is_empty(self):
        return len(self.heap) == 0

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._heapify(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# -------------------- Example Test Code --------------------

if __name__ == "__main__":
    # Heapsort test
    print("Heapsort Test:")
    test_arr = [5, 3, 8, 4, 1, 9, 2]
    print("Original:", test_arr)
    sorted_arr = heapsort(test_arr[:])
    print("Sorted:", sorted_arr)

    # Priority Queue test
    print("\nPriority Queue Test:")
    pq = PriorityQueue()
    pq.insert(Task("T1", 3, 0, 10))
    pq.insert(Task("T2", 5, 1, 8))
    pq.insert(Task("T3", 1, 2, 15))

    print("Extracted:", pq.extract_max())
    pq.increase_key("T3", 6)
    print("Extracted:", pq.extract_max())
    print("Extracted:", pq.extract_max())