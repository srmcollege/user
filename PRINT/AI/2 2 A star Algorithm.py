# Directed graph with edge costs
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

# Heuristic (estimated cost from node to goal) - example values
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

start = 'Vengurla'
goal = 'Kankavli'

# A* Algorithm
open_list = [start]
came_from = {}
g_score = {start: 0}
f_score = {start: heuristic[start]}

while open_list:
    current = min(open_list, key=lambda x: f_score.get(x, float('inf')))
    print("Current node:", current)

    if current == goal:
        print("Goal reached!")
        break

    open_list.remove(current)

    for neighbor, cost in graph[current]:
        tentative_g = g_score[current] + cost
        if tentative_g < g_score.get(neighbor, float('inf')):
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g
            f_score[neighbor] = tentative_g + heuristic[neighbor]
            if neighbor not in open_list:
                open_list.append(neighbor)

else:
    print("No path found.")
    exit()

# Reconstruct path
path = [goal]
while path[-1] in came_from:
    path.append(came_from[path[-1]])
path.reverse()

print("Shortest path:", " -> ".join(path))
print("Total cost:", g_score[goal])
