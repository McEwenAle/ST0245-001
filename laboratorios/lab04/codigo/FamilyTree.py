class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def abuelaMaterna(node):
    return node.left.left

root = Node("Alejandro")
root.left = Node("Ana Maria")
root.right = Node("Juan Guillermo")
root.left.left = Node("Elena")
root.left.right = Node("Agusto")
root.right.left = Node("Paulina")
root.right.right = Node("Juan")
print(abuelaMaterna(root).data)
