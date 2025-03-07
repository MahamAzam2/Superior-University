
from collections import deque

def waterjugproblem_dfs(capacity1, capacity2, goal):
    stack = [(0, 0, [])]  
    visited = set()
    
    while stack:
        state = stack.pop()
        jug1, jug2, path = state  
        
        # Check if target is achieved
        if jug1 == goal or jug2 == goal:
            print("Solution found:")
            for step in path:
                print(step)
            print((jug1, jug2))
            return True
        
        
        if (jug1, jug2) in visited:
            continue
        
        visited.add((jug1, jug2))
        
        # Apply rules 
        stack.append((capacity1, jug2, path + [(jug1, jug2)]))  # Fill jug1
        stack.append((jug1, capacity2, path + [(jug1, jug2)]))  # Fill jug2
        stack.append((0, jug2, path + [(jug1, jug2)]))  # Empty jug1
        stack.append((jug1, 0, path + [(jug1, jug2)]))  # Empty jug2
        
        
        pour_amount = min(jug1, capacity2 - jug2)
        stack.append((jug1 - pour_amount, jug2 + pour_amount, path + [(jug1, jug2)]))   # Pour from jug1 to jug2 until jug2 is full
        
        pour_amount = min(jug2, capacity1 - jug1)
        stack.append((jug1 + pour_amount, jug2 - pour_amount, path + [(jug1, jug2)]))   # Pour from jug2 to jug1 until jug1 is full
    
    print("No solution found")
    return False

jug1Capacity = 4
jug2Capacity = 3
target = 2

waterjugproblem_dfs(jug1Capacity, jug2Capacity, target)
