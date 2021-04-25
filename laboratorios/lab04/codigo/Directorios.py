
class Node:

    def __init__(self, d):
        self.data = d
        self.children = []
    

class Directory:

    def __init__(self, root = None):
        self.root = root

    def search(self, data):
        return self.searchAux(self.root, data)
    
    def searchAux(self, node, data):
        if node == None:
            return None
        if node.data == data:
            return node
        for child in node.children:
            d = self.searchAux(child, data)
            if d != None:
                return d           
        return None

    def add(self, data, parent = None):
        if self.root == None:
            self.root = Node(data)
            return
        p = self.search(parent)
        if p == None:
            return 
        p.children.append(Node(data))

    def remove(self, data):
        parent = self.removeAux(self.root, data)
        if parent == None:
            return None
        return parent[0].children.pop(parent[1])
        

    def removeAux(self, node, data):        
        if node == None:
            return None
        for i in range(len(node.children)):
            if node.children[i] != None and node.children[i].data == data:
                return (node, i)
            d = self.removeAux(node.children[i], data)
            if d != None:
                return d
        return None
    

dir = Directory()
dir.add("home")
dir.add("doc", "home")
dir.add("estrc.txt", "doc")
print("hi")
print(dir.search("estrc.txt").data)
print(dir.remove("estrc.txt").data)
