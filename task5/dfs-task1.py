
tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
}
def DFS_stack(start,goal):
    stack = [start]
    visited = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            stack.extend(reversed(tree[node]))
            
    return visited

visited_nodes = DFS_stack("A" , "G")
print(visited_nodes)