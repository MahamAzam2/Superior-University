#bfs without queue and node
def BFS(graph,start,visited = None):
    if visited is None:
        visited = set()
        
    print(start , end = " ")
    visited.add(start)
    
    for neigbhour in graph[start]:
        if neigbhour not in visited:
            
            BFS(graph,neigbhour,visited)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']    
}
     
start_node = "A"
BFS(graph,start_node)
            
            
        
        
    
    