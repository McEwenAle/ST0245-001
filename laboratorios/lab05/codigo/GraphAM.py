import numpy as np
import queue

class GraphAm:
    def __init__(self, size):
        self.matrix = np.full([size, size], 0)

    def getEdges(self):
        return self.matrix

    def getWeight(self, source, destination):
        return self.matrix[source][destination]

    def addArc(self, source, destination, weight):
        self.matrix[source][destination] = weight 
        self.matrix[destination][source] = weight

    def getSuccessors(self, vertex):
        succ = []
        for i in range(len(self.matrix[vertex])):
            if(self.matrix[vertex][i] != 0):
                succ.append([i, self.matrix[vertex][i]])
        return succ

    def __str__(self):
        s = ""
        for i in range(len(self.matrix)):
            succ = self.getSuccessors(i)
            for e in succ:
                s = s + str(i) + "->" + str(e) + "[ label = \"" + str(self.getWeight(i, e)) + "\"  ]"+ "\n"
        return s

    def Bell_Ford(self, start):
        INF = int(1e9)
        ans = [INF]* len(self.matrix)
        q = queue.Queue()
        ans[start] = 0
        q.put([start, 0])
        while(not q.empty()):
            current = q.get()
            cVertex = current[0]
            cSum = current[1]
            for son in self.getSuccessors(cVertex):
                vertex = son[0]
                weight = son[1]
                nSum = cSum + weight
                if nSum < ans[vertex]:
                    ans[vertex] = nSum
                    q.put([vertex, nSum])
        return ans

graph = GraphAm(5)
graph.addArc(0, 1, 10)
graph.addArc(0, 2, 10)
graph.addArc(0, 3, 14)
graph.addArc(1, 2, 15)
graph.addArc(1, 3, 8)
graph.addArc(2, 3, 12)
graph.addArc(2, 4, 7)
graph.addArc(3, 4, 20)
print(graph.Bell_Ford(0))
print(graph.Bell_Ford(4))
# print(graph.getWeight(2, 4))
# print(graph.getSuccessors(2))
# print(graph)