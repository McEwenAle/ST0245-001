class Node:
    def __init__(self, id, decripcion, next= None) -> None:
        self.id = int(id)
        self.descripcion = str(decripcion)
        self.next = next

class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get(self,index):
        if(index >= self.size): 
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    #No se podria usar la lista enlazada para agregar millones de abejas porque se demoraria segundos por abeja que se añade
    #La complejidad del metodo add es O(n) porque se reccore la lista solo una vez
    def add(self, element, index = -1):
        if(index == -1):
            index = self.size
        if(index > self.size): 
            return -1
        if(index == 0):
            temp = self.head
            self.head = element
            self.head.next = temp
            self.size+=1
            return
        current = self.head
        for i in range(index-1):
            current = current.next
        temp = current.next
        current.next = element
        self.size += 1
    def size(self):
        return self.size
        #La complejidad del metodo remove es O(n) porque se reccore la lista solo una vez
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
    def removeFirst(self):
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp


def nevera(almacen, solicitudes):
    ll = LinkedList(Node(almacen[0][0], almacen[0][1]))
    for i in range(1,len(almacen)):
        ll.add(Node(almacen[i][0], almacen[i][1]), 0)

    for i in range(len(solicitudes) - 1, -1, -1):
        s = ""
        for j in range(solicitudes[i][1]):
            if ll.size == 0:
                print(solicitudes[i][0] + " " + s)
                return
            removed = ll.removeFirst()
            s = s + str(removed.id) + " " + str(removed.descripcion) + " "
        print(solicitudes[i][0] + " " + s)


almacen = [(1,"haceb"), (2,"lg"), (3,"ibm"), (4,"haceb"), (5,"lg"),
(6,"ibm"),(7,"haceb"), (8,"lg"), (9,"ibm"),(8,"lg"), (9,"ibm")]
solicitudes = [("eafit", 10), ("la14", 2), ("olimpica", 4), ("éxito", 1)]
nevera(almacen, solicitudes)




