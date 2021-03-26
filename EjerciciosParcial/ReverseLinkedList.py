
class Node:
    def __init__(self, element , next = None):
        self.data = element
        self.next = next


def reverseLinkedList(head):
    current = head.next
    nxt = head.next.next
    prev = head
    prev.next = None
    while(current.next != None):
        current.next = prev
        prev = current
        current = nxt
        nxt = current.next
    current.next = prev
    return current

head = Node(1)
current = head
for i in range(2, 6):
    current.next = Node(i)
    current = current.next

l = reverseLinkedList(head)
current = l
while(current != None):
    print(current.data)
    current = current.next