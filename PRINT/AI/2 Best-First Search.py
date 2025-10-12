import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = [(heuristic[start], start)]  # (priority, node)
    
    while pq:
        _, current = heapq.heappop(pq)
        print(current, end=" ")

        if current == goal:
            print("\nGoal found!")
            return

        visited.add(current)
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

# Example graph (directed)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'C'],
    'C': ['E'],
    'D': ['F','G'],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

# Heuristic values (lower means closer to goal)
heuristic = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0}

best_first_search(graph, 'A', 'F', heuristic)
