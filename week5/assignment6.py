import random
import time

### --- Selection Algorithms ---

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

def median_of_medians(arr, k):
    if len(arr) < 10:
        return sorted(arr)[k]
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
    pivot = median_of_medians(medians, len(medians)//2)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

### --- Benchmark Test ---

def run_benchmark():
    sizes = [1000, 5000, 10000]
    print(f"{'N':>8} {'Quickselect':>15} {'MedianOfMedians':>18}")
    for size in sizes:
        arr = random.sample(range(size * 2), size)
        k = size // 2
        t1 = time.time()
        quickselect(arr.copy(), k)
        t2 = time.time()
        median_of_medians(arr.copy(), k)
        t3 = time.time()
        print(f"{size:>8} {t2 - t1:>15.6f} {t3 - t2:>18.6f}")

### --- Elementary Data Structures ---

class SimpleArray:
    def __init__(self, size): self.data = [None] * size
    def insert(self, idx, val): self.data[idx] = val
    def access(self, idx): return self.data[idx]
    def delete(self, idx): self.data[idx] = None

class Matrix:
    def __init__(self, r, c): self.data = [[None]*c for _ in range(r)]
    def insert(self, i, j, val): self.data[i][j] = val
    def access(self, i, j): return self.data[i][j]
    def delete(self, i, j): self.data[i][j] = None

class Stack:
    def __init__(self): self.data = []
    def push(self, val): self.data.append(val)
    def pop(self): return self.data.pop()
    def peek(self): return self.data[-1]

class Queue:
    def __init__(self): self.data = []
    def enqueue(self, val): self.data.append(val)
    def dequeue(self): return self.data.pop(0)

class Node:
    def __init__(self, value): self.value = value; self.next = None

class LinkedList:
    def __init__(self): self.head = None
    def insert_front(self, value):
        new = Node(value); new.next = self.head; self.head = new
    def delete(self, value):
        prev, curr = None, self.head
        while curr:
            if curr.value == value:
                if prev: prev.next = curr.next
                else: self.head = curr.next
                return
            prev, curr = curr, curr.next
    def traverse(self):
        curr = self.head
        while curr: print(curr.value, end=" -> "); curr = curr.next
        print("None")

### --- Example Run ---

if __name__ == "__main__":
    print("Benchmarking Selection Algorithms...")
    run_benchmark()

    print("\nData Structure Demo:")
    ll = LinkedList()
    ll.insert_front(3)
    ll.insert_front(2)
    ll.insert_front(1)
    ll.traverse()
    ll.delete(2)
    ll.traverse()