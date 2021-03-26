from collections import deque

def notacionPolaca(cadena):
    operators = "+-*/"
    stack = deque()
    for i in cadena:
        if i not in operators:
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(int(a) + int(b))
            elif i == '-':
                stack.append(int(a) - int(b))
            elif i == '*':
                stack.append(int(a) * int(b))
            elif i == '/':
                stack.append(int(a) / int(b))
    return stack.pop()

# cadena = "35*2+"
# print(notacionPolaca(cadena))

def nevera(almacen, solicitudes):
    ll = deque()
    for i in range(len(almacen)):
        ll.append(almacen[i])

    for i in range(len(solicitudes)):
        s = ""
        currentSolicitud = solicitudes.pop()
        for j in range(currentSolicitud[1]):
            if len(ll) == 0:
                print(currentSolicitud[0] + " " + s)
                return
            removed = ll.pop()
            s = s + str(removed[0]) + " " + str(removed[1]) + " "
        print(currentSolicitud[0] + " " + s)


# almacen = [(1,"haceb"), (2,"lg"), (3,"ibm"), (4,"haceb"), (5,"lg"),
# (6,"ibm"),(7,"haceb"), (8,"lg"), (9,"ibm")]
# solicitudes = [("eafit", 10), ("la14", 2), ("olimpica", 4), ("éxito", 1)]
# nevera(almacen, solicitudes)

def reverseStack(stack):
    reversedStack = deque()
    for i in range(len(stack)):
        reversedStack.append(stack.pop())
    return reversedStack

# stack = deque([1,5,6,9])
# print(stack)
# print(reverseStack(stack))

def atender(queue):
    for i in range(len(queue)):
        p = queue.popleft()
        print("Atendiendo a " + p)

queue = deque()
queue.append("Juan")
queue.append("Maria")
queue.append("Pedro")
atender(queue)
