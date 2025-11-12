
# Objective 

- Implement Linear Search and Binary Search on customer account IDs.
- Understand differences in efficiency.

# Theory

Linear search checks elements sequentially. Binary search divides search space but requires sorted data.

# Algorithm

#### Linear Search

1. Traverse the list sequentially.
2. If element matches target, return found.
3. If end is reached, return not found.

#### Binary Search

1. Sort the list.
2. Find middle element.
3. If middle equals target, return found.
4. If target less, search left half; else right half.
5. Repeat until found or list exhausted.

# Complexity

- Linear Search: O(n)
- Binary Search: O(log n) (after sorting)
