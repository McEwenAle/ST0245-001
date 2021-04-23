import numpy as np

class GraphAm:
    def __init__(self, size):
        self.matrix = np.full([size, size], 0)

    def getEdges(self):
        return self.matrix

    def getWeight(self, source, destination):
        return self.matrix[source][destination]

    def addArc(self, source, destination, weight):
        self.matrix[source][destination] = weight 

    def getSuccessors(self, vertex):
        succ = []
        for i in range(len(self.matrix[vertex])):
            if(self.matrix[vertex][i] != 0):
                succ.append(i)
        return succ

    def __str__(self):
        s = ""
        for i in range(len(self.matrix)):
            succ = self.getSuccessors(i)
            for e in succ:
                s = s + str(i) + "->" + str(e) + "[ label = \"" + str(self.getWeight(i, e)) + "\"  ]"+ "\n"
        return s

    def dfs(self, source, destination):
        visited = np.full([len(self.matrix)], 0)
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

graph = GraphAm(6)
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