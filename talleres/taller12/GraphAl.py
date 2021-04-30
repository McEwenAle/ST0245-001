class GraphAl:
    
    def __init__(self, size):
        self.size = size
        self.lista = [[] for i in range(size)]

    def __repr__(self):
        return '{}'.format(self.lista)

    def getWeight(self, source, destination):
        for d in self.lista[source]:
            if d[0] == destination:
                return d[1]

    def addArc(self, source, destination, weight):
        self.lista[source].append((destination, weight))

    def getSuccessors(self, vertice):
        succs = []
        for d in self.lista[vertice]:
            succs.append(d[0])
        return succs