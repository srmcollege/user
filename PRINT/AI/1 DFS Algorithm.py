
#Depth First Search Algorithm
graph={
"5":["3","7"],
"3":["2","4"],
"2":["3"],
"4":["3","8"],
"7":["5","8"],
"8":["7","4"]
}
visited=set()
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs (visited, graph, neighbour)
            
print("Following is DFS: ")
dfs (visited, graph, "5")



