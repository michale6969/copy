# Objective

- Simulate event processing using queue.
- Add, process, display, and cancel events.

# Theory

Queue supports FIFO order. Deque from collections module provides efficient queue operations.

# Algorithm

1. Add event: append to queue.
2. Process event: pop from front.
3. Cancel event: search and remove if not processed.

# Complexity

- Add/process: O(1)
- Cancel: O(n)
