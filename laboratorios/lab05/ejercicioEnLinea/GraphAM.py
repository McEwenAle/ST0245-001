import numpy as np

class GraphAm:

    def __init__(self, size):
        self.size = size
        self.matriz = np.zeros((size, size))
        
    def __str__(self):
        return f'{self.matriz}'

    def getWeight(self, source, destination):
        return self.matriz[source][destination]

    def addArc(self, source, destination, weight = 1):
        self.matriz[source][destination] = weight
        self.matriz[destination][source] = weight

    def getSuccessors(self, vertex):
        succs = []
        for k, v in enumerate(self.matriz[vertex]):
            if v != 0:
                succs.append(k)
        return succs

