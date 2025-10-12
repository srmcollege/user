from collections import deque

# Map and distances as before
map = {
    'Devgad': ['Vaibhavwadi', 'Kankavli'],
    'Vaibhavwadi': ['Devgad', 'Kankavli'],
    'Kankavli': ['Devgad', 'Vaibhavwadi', 'Kudal', 'Malvan'],
    'Kudal': ['Kankavli', 'Malvan', 'Sawantwadi','Vengurla'],
    'Malvan': ['Kankavli', 'Kudal', 'Vengurla'],
    'Vengurla': ['Malvan', 'Sawantwadi','Kudal'],
    'Sawantwadi': ['Kudal', 'Vengurla', 'Dodamarg'],
    'Dodamarg': ['Sawantwadi']
}

distances = {
    ('Devgad', 'Vaibhavwadi'): 35,
    ('Devgad', 'Kankavli'): 50,
    ('Vaibhavwadi', 'Kankavli'): 25,
    ('Kankavli', 'Kudal'): 30,
    ('Kankavli', 'Malvan'): 40,
    ('Kudal', 'Malvan'): 20,
    ('Kudal', 'Sawantwadi'): 28,
    ('Malvan', 'Vengurla'): 34,
    ('Vengurla', 'Sawantwadi'): 22,
    ('Kudal','Vengurla'): 22,
    ('Sawantwadi', 'Dodamarg'): 26
}

for (a, b), dist in list(distances.items()):
    distances[(b, a)] = dist

# DFS to find all paths + distances
def all_paths(graph, src, dst, path=None, dist=0):
    if path is None:
        path = []
    path = path + [src]

    if src == dst:
        return [(path, dist)]

    paths = []
    for neighbor in graph[src]:
        if neighbor not in path:
            edge_dist = distances.get((src, neighbor), 0)
            paths += all_paths(graph, neighbor, dst, path, dist + edge_dist)
    return paths

# BFS to find shortest path by distance
def shortest_path_bfs(graph, src, dst):
    queue = deque()
    queue.append((src, [src], 0))
    visited = {}

    while queue:
        current, path, cost = queue.popleft()
        if current == dst:
            return path, cost

        for neighbor in graph[current]:
            edge_dist = distances.get((current, neighbor), 0)
            new_cost = cost + edge_dist
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                queue.append((neighbor, path + [neighbor], new_cost))

    return None, float('inf')

# Main code
source = input("Source Taluka: ").title()
destination = input("Destination Taluka: ").title()

if source not in map or destination not in map:
    print("Invalid taluka name.")
else:
    # Find all paths with DFS
    paths = all_paths(map, source, destination)
    print("\nAll Paths (DFS):")
    for i, (p, dist) in enumerate(paths, 1):
        print(f"{i}. {' → '.join(p)} | {dist} km")

    # Find shortest path by BFS
    sp_bfs, dist_bfs = shortest_path_bfs(map, source, destination)
    print("\nShortest Path (BFS):")
    if sp_bfs:
        print(f"{' → '.join(sp_bfs)} | {dist_bfs} km")
    else:
        print("No path found.")

    # Find shortest path by DFS (brute force minimum)
    if paths:
        sp_dfs, dist_dfs = min(paths, key=lambda x: x[1])
        print("\nShortest Path (DFS):")
        print(f"{' → '.join(sp_dfs)} | {dist_dfs} km")
    else:
        print("\nNo path found with DFS.")
