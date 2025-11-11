from collections import deque

# Graph nodes: A, B, C, D, E (index 0 to 4)

# --- Depth-First Search (DFS) with Adjacency Matrix ---
graph_matrix = [
    [0, 1, 1, 0, 0], # A connected to B and C
    [1, 0, 0, 1, 0], # B connected to A and D
    [1, 0, 0, 1, 1], # C connected to A, D, E
    [0, 1, 1, 0, 1], # D connected to B, C, E
    [0, 0, 1, 1, 0]  # E connected to C, D
]

def dfs(node, visited):
    visited[node] = True
    print(chr(node + 65), end=' ') # Convert 0->A, 1->B, etc.
    
    for neighbor in range(len(graph_matrix)):
        # Check if there's an edge (== 1) and it hasn't been visited
        if graph_matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, visited)

print("DFS traversal starting from A:")
visited_dfs = [False] * 5
dfs(0, visited_dfs) # Start at node A (0)


# --- Breadth-First Search (BFS) with Adjacency List ---
graph_list = {
    0: [1, 2],    # A connected to B, C
    1: [0, 3],    # B connected to A, D
    2: [0, 3, 4], # C connected to A, D, E
    3: [1, 2, 4], # D connected to B, C, E
    4: [2, 3]     # E connected to C, D
}

def bfs(start):
    visited_bfs = [False] * 5
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        node = queue.popleft()
        print(chr(node + 65), end=' ')
        
        for neighbor in graph_list[node]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)

print("\nBFS traversal starting from A:")
bfs(0)