import numpy as np
import time
import matplotlib.pyplot as plt

# Row-major sum (cache-friendly)
def row_major_sum(matrix):
    total = 0.0
    for row in matrix:
        for val in row:
            total += val
    return total

# Column-major sum (cache-unfriendly)
def col_major_sum(matrix):
    total = 0.0
    for j in range(matrix.shape[1]):
        for i in range(matrix.shape[0]):
            total += matrix[i, j]
    return total

# Benchmarking function
def benchmark(matrix, trials=5):
    row_times = []
    col_times = []
    for _ in range(trials):
        start = time.perf_counter()
        row_major_sum(matrix)
        row_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        col_major_sum(matrix)
        col_times.append(time.perf_counter() - start)
    return row_times, col_times

# Main execution
if __name__ == "__main__":
    rows, cols = 2000, 2000
    matrix = np.random.rand(rows, cols)
    row_times, col_times = benchmark(matrix)

    print("Trial\tRow-Major (s)\tColumn-Major (s)")
    for i in range(len(row_times)):
        print(f"{i+1}\t{row_times[i]:.4f}\t\t{col_times[i]:.4f}")

    # Plot results
    plt.figure(figsize=(8, 5))
    plt.plot(row_times, label='Row-Major Access (Cache-Friendly)', marker='o')
    plt.plot(col_times, label='Column-Major Access (Cache-Unfriendly)', marker='x')
    plt.title('Cache-Aware vs Cache-Unaware Matrix Access Benchmark')
    plt.xlabel('Trial')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()