
# Objective

- Represent a graph of popular locations as adjacency matrix and adjacency list.
- Perform Depth-First Search (DFS) using adjacency matrix.
- Perform Breadth-First Search (BFS) using adjacency list.
- Determine sequence of visiting locations starting from a given node.

# Theory

A graph is represented by nodes (locations) and edges (routes). DFS explores as far as possible along each branch before backtracking. BFS explores neighbors level by level. Adjacency matrix uses 2D arrays, adjacency list uses lists of neighbours.

# Algorithm

#### DFS using Adjacency Matrix

1. Initialize visited array as False for all nodes.
2. Start at the given node, mark visited, print it.
3. For each adjacent node in matrix, if not visited, recursively call DFS.

#### BFS using Adjacency List

1. Initialize visited array as False and queue.
2. Start at the given node, mark visited, enqueue it.
3. While queue not empty, dequeue node, print it, enqueue all unvisited neighbours.

# Complexity

- DFS using adjacency matrix: O(V^2) where V is number of vertices
- BFS using adjacency list: O(V + E) where E is number of edges
