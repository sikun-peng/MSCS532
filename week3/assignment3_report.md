Assignment 3: Understanding Algorithm Efficiency and Scalability

Student: Sikun Peng
Course: MSCS532
Date: 07/14/2025


Part 1: Randomized Quicksort Analysis

Implementation Summary

We implemented Randomized Quicksort in Python by selecting a pivot uniformly at random from the subarray being sorted. This helps avoid the worst-case behavior that occurs when the pivot is poorly chosen, such as always being the smallest or largest element.

Edge cases considered:
	•	Empty arrays
	•	Arrays with repeated elements
	•	Already sorted and reverse sorted arrays

Theoretical Analysis

Randomized Quicksort’s average-case complexity is O(n log n). This is derived using indicator random variables or recurrence relations. On average, random pivots partition the array evenly, leading to logarithmic depth and linear work per level:
	•	Best case: O(n log n)
	•	Average case: O(n log n)
	•	Worst case: O(n^2) (rare due to random pivot)

Recurrence: T(n) = T(k) + T(n - k - 1) + Θ(n) where k is random

Empirical Comparison

We benchmarked Randomized Quicksort vs. Deterministic Quicksort on:
	•	Random arrays
	•	Sorted arrays
	•	Reverse sorted arrays
	•	Arrays with repeated elements

Results Summary:
	•	Randomized Quicksort outperforms deterministic version on sorted and repeated data
	•	Deterministic Quicksort shows worst-case time on ordered inputs
	•	Empirical trends match theoretical predictions


Part 2: Hash Table with Chaining

Implementation Summary

We implemented a hash table using chaining with lists. Each slot in the table holds a list of key-value pairs. A built-in hash function modulo table size determines the slot index.

Supported operations:
	•	insert(key, value)
	•	search(key)
	•	delete(key)

Theoretical Analysis

Under simple uniform hashing (each key equally likely to hash to any slot), the expected time for all operations is O(1).

Let:
	•	n = number of elements
	•	m = number of slots
	•	Load factor = α = n/m

Then expected time = Θ(1 + α). When α is small, all operations remain constant time on average.

Optimization Strategies
	•	Keep α low by resizing the table when it grows too full
	•	Use universal hash functions to reduce clustering
	•	Rehash when a performance threshold is crossed


Conclusion

This assignment demonstrated the importance of choosing appropriate algorithmic strategies based on input characteristics. Randomized algorithms like Quicksort can mitigate worst-case behavior, while hash tables with chaining offer simple and efficient solutions for dynamic key-value storage. Empirical tests supported the theoretical models well.