class Node:
    def __init__(self,value):
        self.value = value
        self.neighbour= []
        
def bfs(start_node):
        visited = set()
        queue = [start_node]
        visited.add(start_node)  
        
        while queue:
           node = queue.pop(0) 
           print(node.value, end=" ")  

      
           for neighbor in node.neighbors:
               if neighbor not in visited:
                    queue.append(neighbor)  
                    visited.add(neighbor)
                
nodeA = Node("A")
nodeB = Node("B")   
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")

nodeA.neighbors = [nodeB,nodeC]
nodeB.neighbors = [nodeA,nodeD,nodeE]
nodeC.neighbors = [nodeA,nodeF]
nodeD.neighbors = [nodeB]
nodeE.neighbors = [nodeB,nodeF]
nodeF.neighbors = [nodeC,nodeE]

print("bfs with queue and node")
bfs(nodeA)


       
        