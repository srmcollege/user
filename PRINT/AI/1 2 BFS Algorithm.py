from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            # Explore neighbors
            neighbours = graph[vertex]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['D'],
    'H': ['E']
}
# Run BFS starting from node 'A'
bfs(graph, 'A')
