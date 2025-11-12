# Objective

- Implement undo/redo system using stacks.
- Maintain history of changes and allow reversal.

# Theory

Stack supports Last-In-First-Out (LIFO). Two stacks: undo stack stores previous states, redo stack stores undone states.

# Algorithm

1. On new change: push current state to undo stack, clear redo stack.
2. Undo: pop from undo stack to restore state, push current state to redo stack.
3. Redo: pop from redo stack to restore state, push current state to undo stack.
# Complexity

- All operations: O(1)
