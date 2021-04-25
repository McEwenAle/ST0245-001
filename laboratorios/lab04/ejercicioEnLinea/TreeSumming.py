class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def TreeSumming(node, sum, val):#O(2^h)
    left = False
    right = False
    if node.left == None and node.right == None:
        return sum == val
    if node.left != None:
        left = TreeSumming(node.left, sum+node.left.data, val)
    if node.right != None:
        right = TreeSumming(node.right, sum+node.right.data, val)
    return left or right

root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)
print(TreeSumming(root, root.data, 22))