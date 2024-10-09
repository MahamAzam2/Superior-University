#"Inorder, Preorder, Postorder" and implement in DFS



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


def inorder(node):
    if node in tree:
        for child in tree[node][:1]:
            inorder(child)
        print(node ,end = " ")
        
        for child in tree[node][1:]:
            inorder(child)
        
def preorder(node):
    if node in tree:
        print(node ,end = " ")
        for child in tree[node]:
            preorder(child)

def postorder(node):
    if node in tree:
        for child in tree[node]:
            postorder(child)
        print(node ,end = " ")
        
print("\ninorder: ")
inorder("A")

print("\nPreorder: ")
preorder("A")

print("\nPostorder: ")
postorder("A")



