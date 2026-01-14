# AsyncPriorityBuffer: High-Concurrency Resource Management

## Overview
This project implements a prioritized asynchronous task buffer in Python. It addresses the challenge of managing diverse workloads where some tasks require immediate execution (e.g., system heartbeats) while others can tolerate delay (e.g., log cleanup).

## Technical Concepts
### 1. Heap-Based Priority Queue
By utilizing a min-heap (via `heapq`), we ensure that task retrieval is $O(\log n)$, always yielding the highest priority (lowest integer value) task first.

### 2. Backpressure with Asyncio Conditions
The buffer implements a capacity limit. When the buffer is full, producers are suspended using `asyncio.Condition`. This prevents memory exhaustion in systems where production speed outpaces consumption.

### 3. Structured Concurrency
The system uses `dataclasses` for clean state management and `asyncio` workers to simulate a distributed processing environment.

## Why It Matters
In distributed systems, flat FIFO queues lead to \"head-of-line blocking\" where urgent requests wait behind heavy background tasks. This pattern ensures system responsiveness by decoupling task production from consumption while respecting resource constraints.
