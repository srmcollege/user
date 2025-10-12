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

        for neighbor, _ in graph.get(current, []):  # Ignore edge cost
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

# Graph with edge costs (costs are ignored in Best-First Search)
graph = {
    'Devgad': [('Vaibhavwadi', 35), ('Kankavli', 50)],
    'Vaibhavwadi': [('Devgad', 35), ('Kankavli', 25)],
    'Kankavli': [('Devgad', 50), ('Vaibhavwadi', 25), ('Kudal', 30), ('Malvan', 40)],
    'Kudal': [('Vengurla', 22), ('Kankavli', 30), ('Malvan', 20), ('Sawantwadi', 28)],
    'Malvan': [('Kankavli', 40), ('Kudal', 20), ('Vengurla', 50)],
    'Vengurla': [('Kudal', 22), ('Malvan', 50), ('Sawantwadi', 30)],
    'Sawantwadi': [('Kudal', 28), ('Vengurla', 30), ('Dodamarg', 26)],
    'Dodamarg': [('Sawantwadi', 26)]
}

# Heuristic values (lower = closer to goal)
heuristic = {
    'Devgad': 120,
    'Vaibhavwadi': 100,
    'Kankavli': 90,
    'Kudal': 60,
    'Malvan': 70,
    'Vengurla': 50,
    'Sawantwadi': 30,
    'Dodamarg': 0
}

# Define start and goal
start = 'Vengurla'
goal = 'Malvan'

# Run search
best_first_search(graph, start, goal, heuristic)
