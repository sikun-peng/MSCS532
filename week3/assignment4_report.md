Assignment 4: Heap Data Structures - Implementation, Analysis, and Applications

Student: Sikun Peng
Course: MSCS532
Date: 07/14/2025

⸻

1. Heapsort Implementation and Analysis

We implemented the Heapsort algorithm using a max-heap approach. First, we built a max-heap from the input list. Then, we repeatedly extracted the maximum element and placed it at the end of the list, restoring the heap property each time. The entire process sorts the array in-place.

Time Complexity:
	•	Best Case: O(n log n)
	•	Average Case: O(n log n)
	•	Worst Case: O(n log n)

Unlike Quicksort, Heapsort’s time complexity is unaffected by input order. Its performance is consistent due to the structure of the binary heap.

Space Complexity:
	•	In-place sorting with O(1) auxiliary space.


2. Comparison with Quicksort and Merge Sort

We tested Heapsort alongside Randomized Quicksort and Merge Sort across various data configurations:
	•	Randomly ordered
	•	Already sorted
	•	Reverse sorted
	•	Arrays with duplicates

Observations:
	•	Heapsort performed stably across all inputs.
	•	Randomized Quicksort was faster on average but varied more.
	•	Merge Sort performed consistently but used additional memory (O(n)).


3. Priority Queue Implementation

We implemented a binary max-heap-based priority queue for task scheduling. Tasks are represented using a custom Task class containing ID, priority, arrival time, and deadline.

Operations and Time Complexity:
	•	insert(task): O(log n)
	•	extract_max(): O(log n)
	•	increase_key(task_id, new_priority): O(log n)
	•	is_empty(): O(1)

Design Decisions:
	•	Heap via list: Index-based tree operations are efficient in Python.
	•	Max-heap: Suitable for scheduling highest-priority tasks first.
	•	Task abstraction: Supports extensibility for future attributes like CPU burst or I/O type.

Use Cases:
	•	Task scheduling in operating systems
	•	Packet prioritization in networking
	•	Real-time event processing


4. Conclusion

Heaps provide a powerful foundation for both efficient sorting and dynamic priority scheduling. Heapsort offers reliable performance without extra space. The priority queue built on a binary heap supports scalable and responsive task management, aligning well with real-world systems like schedulers and message queues.