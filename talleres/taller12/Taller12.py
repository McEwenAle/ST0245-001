from GraphAl import GraphAl
import queue

def dfs(graph, source, destination):
    return aux_dfs(graph, source, destination, [False]*graph.size)

def aux_dfs(graph, current, destination, visited):
    if current == destination:
        return True
    for son in graph.getSuccessors(current):
        if not visited[son]:
            visited[son] = True
            if aux_dfs(graph, son, destination, visited):
                return True            
    return False

def bfs(graph, source, destination):
    visited = [False]*graph.size
    q = queue.Queue()
    q.put(source)
    while not q.empty():
        current = q.get()
        if current == destination:
            return True
        for son in graph.getSuccessors(current):
            if not visited[son]:
                visited[son] = True
                q.put(son)
    return False

def print_dfs(graph, source):
    return aux_print_dfs(graph, source, [False]*graph.size)

def aux_print_dfs(graph, current, visited):
    print(current)
    for son in graph.getSuccessors(current):
        if not visited[son]:
            visited[son] = True
            aux_print_dfs(graph, son, visited)

def print_bfs(graph, source):
    visited = [False]*graph.size
    q = queue.Queue()
    q.put(source)
    while not q.empty():
        current = q.get()
        print(current)
        for son in graph.getSuccessors(current):
            if not visited[son]:
                visited[son] = True
                q.put(son)


g = GraphAl(6)
g.addArc(1, 4, 3)
g.addArc(2, 4, 1)
g.addArc(1, 2, 5)
g.addArc(5, 4, 2)
g.addArc(3, 2, 2)
g.addArc(4, 3, 6)
print(dfs(g, 1, 3))
print(bfs(g, 1, 3))
print(dfs(g, 1, 5))
print(bfs(g, 1, 5))
print_dfs(g, 1)
print_bfs(g, 1)
