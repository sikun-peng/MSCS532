# Cache-Aware Matrix Access Benchmark

This project demonstrates the performance difference between cache-aware (row-major) and cache-unaware (column-major) matrix access patterns using NumPy in Python.

## Concept

Modern CPUs use caches to speed up memory access. Accessing data in a row-wise (cache-friendly) order takes advantage of spatial locality, leading to significant speedup.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt