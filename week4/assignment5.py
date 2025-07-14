import time
import random

# -------------------------------
# Deterministic Quicksort
# -------------------------------

def deterministic_quicksort(arr):
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(arr, 0, len(arr) - 1)
    return arr

# -------------------------------
# Randomized Quicksort
# -------------------------------

def randomized_quicksort(arr):
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = randomized_partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    def randomized_partition(arr, low, high):
        rand_pivot_index = random.randint(low, high)
        arr[high], arr[rand_pivot_index] = arr[rand_pivot_index], arr[high]
        return partition(arr, low, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(arr, 0, len(arr) - 1)
    return arr

# -------------------------------
# Benchmarking
# -------------------------------

def generate_input(size, kind="random"):
    if kind == "sorted":
        return list(range(size))
    elif kind == "reversed":
        return list(range(size, 0, -1))
    elif kind == "random":
        return random.sample(range(size * 2), size)
    else:
        raise ValueError("Unknown input type")

def benchmark():
    sizes = [1000, 5000, 10000]
    types = ["random", "sorted", "reversed"]

    for size in sizes:
        for kind in types:
            data = generate_input(size, kind)
            print(f"\n--- Size: {size}, Type: {kind} ---")

            start = time.time()
            deterministic_quicksort(data[:])
            print(f"Deterministic: {time.time() - start:.5f} sec")

            start = time.time()
            randomized_quicksort(data[:])
            print(f"Randomized:   {time.time() - start:.5f} sec")

if __name__ == "__main__":
    benchmark()