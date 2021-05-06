from GraphAM import GraphAm 

def bipartiteness(graph, source):
    return aux_bipartiteness(graph, source, [0]*graph.size, 1)

def aux_bipartiteness(graph, current, visited, color):
    for son in graph.getSuccessors(current):
        if visited[son] == 0:
            visited[son] = color
            aux_bipartiteness(graph, son, visited, color%2 +1)
            if not aux_bipartiteness(graph, son, visited, color%2 +1):
                return False
        elif visited[current] == visited[son]:
            return False
    return True

n = int(input())

while(n != 0):
    g = GraphAm(n)
    arc = int(input())
    for i in range(arc):
        a,b = input().split()
        g.addArc(int(a), int(b))
    if bipartiteness(g, 0):
        print('BICOLORABLE.')
    else:
        print('NOT BICOLORABLE.')
    n = int(input())
    
    
