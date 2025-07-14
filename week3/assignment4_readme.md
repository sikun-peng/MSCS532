Assignment 4: Heap Data Structures - Heapsort and Priority Queue

Overview

This repository contains Python implementations of:
	•	Heapsort Algorithm for in-place sorting
	•	Priority Queue using a max-heap for task scheduling

These implementations are part of a course assignment to understand heap data structures, analyze time complexity, and demonstrate real-world applications.

Contents
	•	assignment4.py: Contains both Heapsort and PriorityQueue implementations
	•	report.md: Detailed report explaining design choices and complexity analysis
	•	README.md: Instructions and summary (this file)

How to Run

Prerequisites
	•	Python 3.x

Execute the script

python assignment4_heaps.py

This will:
	•	Sort a sample array using Heapsort
	•	Demonstrate priority queue operations like insert, extract_max, and increase_key


Features

Heapsort
	•	Builds a max-heap and sorts in O(n log n) time
	•	Uses no extra memory (in-place)
Priority Queue
	•	Based on a binary max-heap
	•	Supports:
	•	insert(task)
	•	extract_max()
	•	increase_key(task_id, new_priority)
	•	is_empty()
	•	Includes a Task class with ID, priority, arrival time, and deadline


Time Complexity Summary

Operation	Time Complexity
Heapsort	O(n log n)
insert	O(log n)
extract_max	O(log n)
increase_key	O(log n)
is_empty	O(1)
