import numpy as np

class GraphAL:
    def __init__(self, size):
        self.array = []
        for i in range(size):
            self.array.append([])

    def addArc(self, vertex, edge, weight):
        self.array[vertex].append((edge, weight))

    def getSuccessors(self, vertice):
        l = []
        for edge, weight in self.array[vertice]:
            l.append(edge)
        return l

    def getWeight(self, source, destination):
        for edge, weight in self.array[source]:
            if edge == destination:
                return weight
        return 0

    def __str__(self):
        s = ""
        for vertex in range(len(self.array)):
            for edge, weight in self.array[vertex]:
                s = s + str(vertex) + "->" + str(edge) + "[ label = \"" + str(weight) + "\"  ]"+ "\n"
        return s
    
    def dfs(self, source, destination):
        visited = np.full([len(self.array)], 0)
        return self.aux_dfs(source, destination, visited)
    
    def aux_dfs(self, current, destination, visited):
        if current == destination:
            return True
        succ = self.getSuccessors(current)
        for e in succ:
            if not visited[e]:
                visited[e] = True
                if self.aux_dfs(e, destination, visited):
                    return True
        return False




graph = GraphAL(5)
graph.addArc(0, 4, 1)
graph.addArc(1, 3, 1)
graph.addArc(3, 2, 1)
graph.addArc(2, 4, 2)
graph.addArc(4, 3, 1)
graph.addArc(2,3, 1)
print(graph.dfs(1,4))
print(graph.dfs(0,5))
# print(graph.getWeight(2, 4))
# print(graph.getSuccessors(2))
# print(graph)