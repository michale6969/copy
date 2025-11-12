from collections import deque

# --- Graph Definitions (Unchanged) ---
# Graph nodes: A, B, C, D, E (index 0 to 4)
graph_matrix = [
    [0, 1, 1, 0, 0], # A
    [1, 0, 0, 1, 0], # B
    [1, 0, 0, 1, 1], # C
    [0, 1, 1, 0, 1], # D
    [0, 0, 1, 1, 0]  # E
]

graph_list = {
    0: [1, 2],    # A connected to B, C
    1: [0, 3],    # B connected to A, D
    2: [0, 3, 4], # C connected to A, D, E
    3: [1, 2, 4], # D connected to B, C, E
    4: [2, 3]     # E connected to C, D
}

# --- DFS Function (Unchanged) ---
def dfs(node, visited):
    visited[node] = True
    print(chr(node + 65), end=' ') # Convert 0->A, 1->B, etc.
    
    for neighbor in range(len(graph_matrix)):
        if graph_matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, visited)

# --- BFS Function (Unchanged) ---
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

# --- New Interactive Loop ---

# Helper to map 'A' -> 0, 'B' -> 1, etc.
def get_node_index(char):
    char = char.upper()
    if 'A' <= char <= 'E':
        return ord(char) - 65 # 'A' is 65, so 'A' -> 0
    return -1 # Invalid input

print("--- Graph Traversal ---")
print("Graph Nodes: A, B, C, D, E")

while True:
    print("\nSelect algorithm:")
    print("(1) Depth-First Search (DFS) - uses Adjacency Matrix")
    print("(2) Breadth-First Search (BFS) - uses Adjacency List")
    print("(3) Quit")
    choice = input("Enter choice (1-3): ").strip()

    if choice == '1':
        # --- Run DFS ---
        start_char = input("Enter start node (A-E): ")
        start_node = get_node_index(start_char)
        
        if start_node == -1:
            print("Invalid node. Please enter A, B, C, D, or E.")
            continue # Ask for algorithm again
            
        print(f"DFS traversal starting from {start_char.upper()}:")
        visited_dfs = [False] * 5
        dfs(start_node, visited_dfs)
        print() # For newline
        
    elif choice == '2':
        # --- Run BFS ---
        start_char = input("Enter start node (A-E): ")
        start_node = get_node_index(start_char)
        
        if start_node == -1:
            print("Invalid node. Please enter A, B, C, D, or E.")
            continue # Ask for algorithm again
            
        print(f"BFS traversal starting from {start_char.upper()}:")
        bfs(start_node)
        print() # For newline
        
    elif choice == '3':
        print("Goodbye!")
        break # Exit the while loop
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
