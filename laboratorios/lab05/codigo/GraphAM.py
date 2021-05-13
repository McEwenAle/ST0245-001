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

size = 5
timeDifference = 4
graph = GraphAm(5)
graph.addArc(0, 1, 10)
graph.addArc(0, 2, 10)
graph.addArc(0, 3, 14)
graph.addArc(1, 2, 15)
graph.addArc(1, 3, 8)
graph.addArc(2, 3, 12)
graph.addArc(2, 4, 7)
graph.addArc(3, 4, 3)
shortestPath = [0]*size
for i in range(size):
    shortestPath[i] = graph.Bell_Ford(i)

pairs = []
for i in range(size):
    pairs.append([])

#Parejas
for i in range(1, size):
    for j in range(1,size):
        if i == j:
            continue
        if shortestPath[i][j] + shortestPath[j][0] <= shortestPath[i][0] + timeDifference:
            pairs[i].append((i,j))

triplets = []

#Combinations
for e in pairs:
    for p in e:
        first = p[0]
        second = p[1]
        for match in pairs[second]:
            third = match[1]
            if first == third:
                continue
            if shortestPath[first][second] + shortestPath[second][third] + shortestPath[third][0] <= shortestPath[i][0] + timeDifference:
                triplets.append((first, second, third))

quadruplets = []

#Combinations
for e in triplets:
    first = e[0]
    second = e[1]
    third = e[2]
    for match in pairs[third]:
        fourth = match[1]
        if first == fourth or second == fourth:
            continue
        if shortestPath[first][second] + shortestPath[second][third] + shortestPath[third][fourth] + shortestPath[fourth][0] <= shortestPath[i][0] + timeDifference:
            quadruplets.append((first, second, third, fourth))

groups = []
for e in quadruplets:
    groups.append(e)

for e in triplets:  
    groups.append(e)

for i in range(size):
    for e in pairs[i]:
        groups.append(e)

visited = [False]*size


#mininum
def minimum(i, selected = []):
    if i == len(groups):
        l = []
        for n in selected:
            l.append(groups[n])
        return l
    passed = True
    for e in groups[i]:
        if visited[e]:
            passed = False
    if passed:
        for e in groups[i]:
            visited[e] = True
        selected.append(i)
        cL = minimum(i+1, selected)
        for e in groups[i]:
            visited[e] = False
    nL = minimum(i+1, selected)
    if not passed:
        return nL
    if len(cL) <= len(nL):
        return cL
    else:
        return nL

ans = minimum(0)
for e in ans:
    for ee in e:
        visited[ee] = True

for i in range(1,size):
    if not visited[i]:
        ans.append((i))

print(ans)
    

