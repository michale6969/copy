# Objective

- Implement hashtable of fixed size using linear probing collision resolution.
- Support insert, search, delete, display operations.

# Theory

On collision, linearly probe next slot. Handle wrap-around with modulo arithmetic.

# Algorithm

1. Insert: probe next index till empty or duplicate.
2. Search: probe until key found or empty slot.
3. Delete: mark slot as deleted to handle probing.

# Complexity

- Average: O(1)
