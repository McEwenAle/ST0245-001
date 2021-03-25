class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return "" + self.data

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self,index):
        if(index >= self.size): 
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    def add(self, element, index = -1):
        if(index == -1):
            index = self.size
        if(index > self.size): 
            return -1
        if(index == 0):
            temp = self.head
            self.head = Node(element, temp)
            self.size+=1
            return
        current = self.head
        for i in range(index-1):
            current = current.next
        temp = current.next
        current.next = Node(element, temp)
        self.size += 1
    def size(self):
        return self.size
    def remove(self, index):
        if(index >= self.size): 
            return -1
        current = self.head
        if(index == 0):
            self.head = self.head.next
            self.size -= 1
            return
        for i in range(index-1):
            current = current.next
        current.next = current.next.next
        self.size -= 1
    def contains(self, element):
        current = self.head
        for i in range(self.size):
            if(current.data == element):
                return i
            current = current.next
        return -1
    def maximum(self, m=0, node = -1):
        if(node == -1):
            node = self.head
        if(node == None):
            return m
        m = max(m, node.data)
        return self.maximum(m, node.next)
    def equals(self, l, node = -1, nodel = -1):
        if(node == -1 or nodel == -1):
            node = self.head
            nodel = l.head
        if(node == None and nodel == None):
            return True        
        if(self.size != l.size or node.data != nodel.data):
            return False
        return self.equals(l, node.next, nodel.next)

    def __str__(self) -> str:
        s = ""
        current = self.head
        while current != None:
            s = s + str(current)
            current = current.next
        return s



while True:
    try:
        entrada = input()
    except EOFError:
        break
    s = LinkedList()
    pos = 0
    for c in entrada:
        if c == "[":
            pos = 0
        elif c == "]":
            pos = s.size
        else:
            s.add(c, pos)
            pos += 1
    print(s)
