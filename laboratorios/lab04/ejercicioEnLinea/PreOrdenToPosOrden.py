class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def addAux(self, node, data):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
                return
            self.addAux(node.left, data)
            return
        if node.right == None:
            node.right = Node(data)
            return
        self.addAux(node.right, data)


    def add(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        self.addAux(self.root, data)
        
    def posOrderAux(self, node):
        left = ""
        right = ""
        if node.left != None:
            left = self.posOrderAux(node.left) + "\n"
        if node.right != None:
            right = self.posOrderAux(node.right) + "\n"
        return left + right + str(node.data)
        

    def posOrder(self):
        return self.posOrderAux(self.root)

def PreToPos():
    bT = BinarySearchTree()
    s = input()
    while(s != ""):
        a = int(s)
        bT.add(a)
        s = input()
    return bT.posOrder()

print(PreToPos())