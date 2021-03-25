class Node:
    def __init__(self, val, next = None, prev = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)

class LinkedListMauricio:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, elem, i = -1):
        node = Node(elem)
        if i < -1 or self.size < i:
            return
        elif self.size == 0:
            self.head = node
            self.tail = node
        elif i == -1:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            current = self.head
            for k in range(i):
                current = current.next
            temp = current.next
            current.next = node
            node.prev = current
            node.next = temp
            if temp != None:
                temp.prev = node
        self.size += 1

    def remove(self, i = -1):
        if i < -1 or self.size < i or self.size == 0:
            return
        elif i == -1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for k in range(i - 1):
                current = current.next
            if current.next.next != None:
                current.next.next.prev = current.prev
            current.next = current.next.next
        self.size -= 1

    def contains(self, elem):
        current = self.head
        while(current != None):
            if elem == current.val:
                return True
            current = current.next
        return False

    def __str__(self) -> str:
        current = self.head
        s = ""
        while(current != None):
            s = s + str(current) + " <-> "
            current = current.next
        s = s + "None"
        return s


# dL = LinkedListMauricio()
# dL.add(1)
# dL.add(2)
# dL.add(3, 1)
# print(dL)
# dL.remove(0)
# print(dL)
# print(dL.contains(0))
# print(dL.contains(3))

