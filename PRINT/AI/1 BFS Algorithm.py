# breadth first search algorithm
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
    "VENGURLA":["SAWANTWADI","MALVAN","KUDAL"],
    "SAWANTWADI":["VENGURLA","DODAMARG","KUDAL"],
    "DODAMARG":["SAWANTWADI"],
    "KUDAL":["VENGURLA","SAWANTWADI","MALVAN","KANKAVLI"],
    "MALVAN":["VENGURLA","KUDAL","KANKAVLI","DEVGAD"],
    "VAIBHAVWADI":["KANKAVLI"],
    "DEVGAD":["KANKAVLI","MALVAN"],
    "KANKAVLI":["DEVGAD","VAIBHAVWADI","MALVAN","KUDAL"],
}

# Run BFS starting from node
source=input("Enter a source: ")
bfs(graph, source)
