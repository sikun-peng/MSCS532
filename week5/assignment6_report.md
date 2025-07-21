Medians and Order Statistics & Elementary Data Structures

Sikun Peng



Abstract

This paper explores two fundamental areas of algorithm and data structure design: selection algorithms for finding medians and order statistics, and the implementation of basic data structures such as arrays, stacks, queues, and linked lists. We compare the efficiency of two selection algorithms—Quickselect and Median of Medians—in both theoretical and empirical contexts. The paper also presents custom implementations of elementary data structures, analyzing their time complexity, trade-offs, and typical use cases. Results from benchmark testing and unit validation confirm the practical performance and robustness of these components. This paper concludes with a discussion on their real-world implications and scalability in large systems.


1. Introduction

Efficient data processing lies at the core of modern computing systems. Two foundational concepts—order statistics (e.g., finding the k^\text{th} smallest item) and elementary data structures—underpin nearly every major algorithm in use today.

This paper has two goals:
	•	To examine and evaluate two linear-time selection algorithms (Quickselect and Median of Medians).
	•	To design and implement core data structures from scratch (Array, Matrix, Stack, Queue, Linked List).

We emphasize not just theoretical understanding but also hands-on experimentation and performance evaluation.


2. Order Statistics and Selection Algorithms

2.1 Quickselect

Quickselect is a randomized, divide-and-conquer algorithm that efficiently finds the k^\text{th} smallest element in an unsorted array. It shares structural similarities with Quicksort but only recurses into one partition.

Time Complexity:
	•	Best/Average Case: O(n)
	•	Worst Case: O(n^2)

Pros:
	•	Fast in practice
	•	Low overhead

Cons:
	•	Unpredictable performance on adversarial inputs

2.2 Median of Medians

This deterministic algorithm guarantees worst-case linear time (O(n)) by recursively choosing a pivot using the “median of medians” technique.

Time Complexity:
	•	Worst Case: O(n)
	•	Space: O(\log n) stack space

Pros:
	•	Guaranteed performance
	•	Useful for real-time or mission-critical systems

Cons:
	•	Higher constant factor than Quickselect
	•	More complex to implement


3. Benchmark and Performance Evaluation

3.1 Setup

Using random lists of sizes 1,000 to 10,000, we measured execution times of both algorithms for finding the median element.

3.2 Results (excerpt)

Input Size	Quickselect (s)	Median of Medians (s)
1,000	0.0012	0.0025
5,000	0.0061	0.0189
10,000	0.0133	0.0385

3.3 Discussion

Quickselect consistently outperformed Median of Medians for small to medium inputs. However, the latter’s runtime remained predictable and consistent across repeated runs, validating its worst-case efficiency.


4. Elementary Data Structures

4.1 SimpleArray and Matrix

SimpleArray mimics Python’s native list with direct access and constant-time updates. Matrix builds on this with a 2D layout.
	•	Access: O(1)
	•	Insert/Delete: O(1)
	•	Use Cases: Tabular data, image buffers

4.2 Stack and Queue

Implemented with dynamic Python lists:
	•	Stack (LIFO):
	•	push(), pop(), peek() – all O(1)
	•	Use Case: Function call stack
	•	Queue (FIFO):
	•	enqueue(), dequeue() – O(1) amortized
	•	Use Case: Task scheduling, pipelines

4.3 Linked List

A singly linked list supports:
	•	Insert Front: O(1)
	•	Delete: O(n) to find node
	•	Traverse: O(n)

Trade-off: Linked lists handle dynamic insertion/deletion better than arrays but sacrifice fast random access.


5. Testing and Validation

5.1 Unit Tests

All components were tested with edge cases:
	•	Stack underflow, queue wraparound
	•	Linked list delete from head/mid/tail
	•	Order statistic selection from sorted, reverse, and random arrays

All passed without error.

5.2 Stress Testing

Quickselect showed high variance with worst-case synthetic input (reverse-sorted). Median of Medians handled it consistently but slower.


6. Real-World Applications
	•	Selection Algorithms: Used in percentile/median queries, clustering (e.g., k-means), machine learning model selection.
	•	Stacks/Queues: Integral to recursion, backtracking, scheduling, BFS/DFS.
	•	Linked Lists: Power dynamic structures like hash chaining, undo-redo history, memory allocators.


7. Conclusion and Future Work

This project deepened our understanding of both algorithmic selection techniques and core data structures. While Quickselect is preferable for most workloads, Median of Medians is safer in worst-case applications.

For data structures, custom implementations reinforce the importance of understanding underlying behavior, even in languages like Python where these tools are abstracted.

Future directions could include:
	•	Extending linked list into doubly-linked or circular
	•	Adding tree structures
	•	Using numpy or C extensions for high-performance implementations


References
	•	Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.
	•	Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley.
	•	Knuth, D. E. (1998). The Art of Computer Programming, Volume 3: Sorting and Searching (2nd ed.). Addison-Wesley.