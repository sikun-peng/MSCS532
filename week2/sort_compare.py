# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Benchmark function
import time
import tracemalloc

def benchmark_sorting_algorithm(sort_func, data):
    tracemalloc.start()
    start_time = time.perf_counter()
    sort_func(data.copy())
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak

# Generate datasets
import random
sizes = [100, 1000, 5000, 10000]
datasets = {
    "Sorted": [list(range(n)) for n in sizes],
    "Reverse Sorted": [list(range(n, 0, -1)) for n in sizes],
    "Random": [random.sample(range(n), n) for n in sizes],
}

# Run benchmarks
results = []
for data_type, data_lists in datasets.items():
    for size, data in zip(sizes, data_lists):
        for algo_name, algo_func in [("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]:
            exec_time, memory = benchmark_sorting_algorithm(algo_func, data)
            results.append({
                "Algorithm": algo_name,
                "Dataset Type": data_type,
                "Input Size": size,
                "Execution Time (s)": exec_time,
                "Memory Usage (bytes)": memory
            })

# Display results
import pandas as pd
df = pd.DataFrame(results)
print(df)