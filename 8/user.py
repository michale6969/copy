import heapq

def dijkstra(graph, start):
    # Check if the start node is valid
    if start not in graph:
        print(f"Error: Start node {start} not in graph.")
        return None
        
    n = len(graph)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)] # (distance, node)
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if dist > distances[node]:
            continue
            
        # Use .get() to safely handle nodes that might not have neighbors
        for neighbor, weight in graph.get(node, []):
            # Ensure neighbor is in the distances dict
            if neighbor not in distances:
                continue
                
            new_dist = dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                
    return distances

# Graph represented as adjacency list with weights
# Node 0 = Pizza shop, nodes 1-4 = customer locations
graph = {
    0: [(1, 10), (2, 15)],
    1: [(0, 10), (3, 12), (4, 15)],
    2: [(0, 15), (4, 10)],
    3: [(1, 12), (4, 2)],
    4: [(1, 15), (2, 10), (3, 2)]
}

# --- New Interactive Loop ---
print("--- Dijkstra's Shortest Path (Pizza Delivery) ---")
print(f"Locations are: {list(graph.keys())}")

while True:
    start_input = input("\nEnter start location (or 'quit'): ").strip()
    
    if start_input.lower() == 'quit':
        print("Goodbye!")
        break
        
    try:
        start_node = int(start_input)
        
        # Calculate distances
        distances = dijkstra(graph, start_node)
        
        if distances:
            print(f"\nMinimum time from Location {start_node} to each location:")
            for node, dist in distances.items():
                print(f"  -> Location {node}: {dist} minutes")
                
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
