# Objective

- Manage borrowing records of books in a library.
- Compute average number of books borrowed.
- Find books with highest and lowest borrowings.
- Count members with zero borrowings.
- Find the most frequently borrowed book count (mode).

# Theory

Use dictionaries to store book borrowing counts. Compute statistical values using loops and collections.

# Algorithm

1. Store book borrowing data in a dictionary: `{book_id: borrow_count}`.
2. Calculate average by summing all borrow counts and dividing by total books.
3. Find max and min borrowing counts by scanning the dictionary.
4. Count books with borrow count zero.
5. Use a frequency map to find mode (most frequent borrow count).

# Complexity 

- Time Complexity: O(n)
- Space Complexity: O(n)
