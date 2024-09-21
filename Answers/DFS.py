def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set to track visited nodes

    visited.add(start)  # Mark the current node as visited
    print(start, end=" ")  # Process the current node (printing it)

    # Recursively visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start DFS from vertex 'A'
dfs(graph, 'B')