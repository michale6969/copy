
# Objective

- Model pizza delivery locations as graph nodes.
- Edges represent time to travel between locations.
- Find the minimum total time to deliver pizza to all customers.
- Use appropriate graph algorithms and data structures.

# Theory

The problem is a variation of the Travelling Salesman Problem (TSP) or shortest path covering all nodes. Since exact TSP is NP-hard, heuristic or shortest path algorithms (like Dijkstra or BFS for unweighted) can be applied depending on data.

# Algorithm (Using Dijkstra’s Algorithm)

1. Represent locations as graph nodes and travel times as edge weights.
2. From the pizza shop starting node, use Dijkstra's algorithm to find shortest paths to all delivery locations.
3. Sum shortest path times or find minimum route covering all nodes (approximate).

# Complexity

- Dijkstra's algorithm: O(E log V) where E is edges, V is vertices.
