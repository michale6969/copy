# Objective

- Implement hashtable of size 10 using chaining.
- Handle insert, search, and delete operations.

# Theory

Hash function: key % 10. Collisions handled by storing multiple elements in a bucket (list).

# Algorithm

1. Insert: compute index, append if no duplicate.
2. Search: scan bucket list.
3. Delete: remove from bucket list.

# Complexity

- Average: O(1)
- Worst-case: O(n)
