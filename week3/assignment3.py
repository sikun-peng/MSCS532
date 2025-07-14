import random
import time
import matplotlib.pyplot as plt

# -------------------- Part 1: Randomized Quicksort --------------------

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

def benchmark_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]
    types = ['random', 'sorted', 'reverse', 'repeated']
    results = []

    for size in sizes:
        for t in types:
            if t == 'random':
                arr = [random.randint(0, 10000) for _ in range(size)]
            elif t == 'sorted':
                arr = list(range(size))
            elif t == 'reverse':
                arr = list(range(size, 0, -1))
            elif t == 'repeated':
                arr = [5] * size

            r_arr = arr[:]
            d_arr = arr[:]

            start = time.time()
            randomized_quicksort(r_arr)
            r_time = time.time() - start

            start = time.time()
            deterministic_quicksort(d_arr)
            d_time = time.time() - start

            results.append((size, t, r_time, d_time))

    return results

# -------------------- Part 2: Hash Table with Chaining --------------------

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

# -------------------- Run Benchmark --------------------
if __name__ == '__main__':
    result_data = benchmark_sorting_algorithms()
    for size, dtype, r_time, d_time in result_data:
        print(f"Size: {size}, Type: {dtype}, Randomized: {r_time:.5f}s, Deterministic: {d_time:.5f}s")

    # Hash Table test
    ht = HashTable()
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    print(ht.search("banana"))  # 20
    ht.delete("banana")
    print(ht.search("banana"))  # None