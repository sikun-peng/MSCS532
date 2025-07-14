Assignment 3: Algorithm Efficiency and Scalability

Overview

This project implements and analyzes two fundamental algorithmic techniques:
	•	Randomized Quicksort vs. Deterministic Quicksort
	•	Hash Table with Chaining for collision resolution

We examine both theoretical complexity and empirical performance using Python.


Files
	•	assignment3_algorithms.py: Main Python file containing all implementations
	•	report.md: Theoretical analysis, performance comparisons, and findings
	•	README.md: This document


How to Run

Requirements
	•	Python 3.x
	•	matplotlib (for visualizations if extended)

Execute Sorting Benchmarks

python assignment3_algorithms.py

This will:
	•	Compare randomized vs. deterministic quicksort on different input types
	•	Demonstrate operations on a simple hash table using chaining


Features

Randomized Quicksort
	•	Pivot selected randomly
	•	Handles duplicates, sorted and reverse inputs

Deterministic Quicksort
	•	Uses first element as pivot
	•	Included for benchmarking comparison

Hash Table with Chaining
	•	Collision resolution using lists
	•	Supports:
	•	insert(key, value)
	•	search(key)
	•	delete(key)



Complexity Summary

Component	Best / Average / Worst Case
Randomized Quicksort	O(n log n) / O(n log n) / O(n^2)
Deterministic Quicksort	O(n log n) / O(n log n) / O(n^2)
Hash Insert/Search/Delete	O(1) expected, O(n) worst
