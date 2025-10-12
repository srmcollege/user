#Depth First Search Algorithm
graph={
       "VENGURLA":["SAWANTWADI","MALVAN","KUDAL"],
       "SAWANTWADI":["VENGURLA","DODAMARG","KUDAL"],
       "DODAMARG":["SAWANTWADI"],
       "KUDAL":["VENGURLA","SAWANTWADI","MALVAN","KANKAVLI"],
       "MALVAN":["VENGURLA","KUDAL","KANKAVLI","DEVGAD"],
       "VAIBHAVWADI":["KANKAVLI","DEVGAD"],
       "DEVGAD":["KANKAVLI","VAIBHAVWADI","MALVAN"],
       "KANKAVLI":["DEVGAD","VAIBHAVWADI","MALVAN","KUDAL"],

}
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("Following is DFS: ")
dfs(visited,graph,"DEVGAD")

