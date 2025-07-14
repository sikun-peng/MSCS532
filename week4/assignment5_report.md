Quicksort Algorithm: Implementation, Analysis, and Randomization

1. Introduction

Quicksort is a divide-and-conquer sorting algorithm widely used due to its efficiency and in-place sorting nature. It works by selecting a pivot element, partitioning the array into elements less than and greater than the pivot, and recursively sorting the subarrays. While its average-case time complexity is O(n \log n), poor pivot choices can degrade performance to O(n^2). This report explores both deterministic and randomized versions of Quicksort and analyzes their theoretical and empirical performance.


2. Deterministic Quicksort

The deterministic Quicksort algorithm always uses a fixed strategy to choose the pivot — in this case, the last element of the subarray. Although simple to implement, this approach can lead to imbalanced partitions on sorted or nearly sorted input.

Time Complexity:
	•	Best Case: O(n \log n) — when partitions are balanced.
	•	Average Case: O(n \log n)
	•	Worst Case: O(n^2) — occurs when the pivot is the smallest or largest element every time (e.g., sorted array).

Space Complexity:
	•	In-place, uses O(\log n) space on average for recursive stack frames.

3. Randomized Quicksort

Randomized Quicksort improves on the deterministic version by selecting a pivot randomly within the current subarray. This probabilistic approach reduces the chance of consistently poor pivot choices and helps avoid worst-case behavior.

Benefits of Randomization:
	•	Maintains O(n \log n) expected runtime regardless of input order.
	•	Avoids worst-case performance for adversarial input patterns.
	•	Preserves in-place sorting and average-case efficiency.

Randomization makes Quicksort more robust for use in general-purpose libraries and systems where input characteristics are unknown.


4. Empirical Analysis

Both versions were benchmarked using input arrays of size 1,000 to 10,000 with three input types:
	•	Random
	•	Sorted
	•	Reverse-sorted

Findings:
	•	Deterministic Quicksort performed well on random inputs but slowed significantly on sorted and reverse-sorted inputs, due to unbalanced partitioning.
	•	Randomized Quicksort showed consistent performance across all input types, confirming its resilience to input order.
	•	As input size increased, the performance gap between the two versions widened, especially on worst-case patterns.

These results align with the theoretical analysis and reinforce the advantage of introducing randomness into pivot selection.


5. Conclusion

Randomized Quicksort is a simple yet powerful modification of the classic Quicksort algorithm. It combines the efficiency of in-place sorting with robustness against pathological input patterns. For applications requiring consistent performance across unpredictable datasets — such as sorting logs, database records, or web traffic — randomized Quicksort is the preferred choice.