from Mapa import Node, Connection
import pandas as pd


dataVertices = pd.read_csv('Vertices.csv')
dataVertices.columns = ["ID","CoordenadaX","CoordenadaY","Nombre"]
Nodes = [0] * (len(dataVertices["ID"]) + 1)
for i in dataVertices["ID"]:
    Nodes[i] = Node(i, dataVertices["CoordenadaX"][i - 1], dataVertices["CoordenadaY"][i - 1], dataVertices["Nombre"][i - 1])






dataArcos = pd.read_csv('Arcos.csv')
dataArcos.columns = ["ID","ID1","Distancia","Nombre"]
for i in range(len(dataArcos["ID"])):
    Nodes[dataArcos["ID"][i]].addConection(dataArcos["ID1"][i], dataArcos["Distancia"][i], str(dataArcos["Nombre"][i]))
    Nodes[dataArcos["ID1"][i]].addConection(dataArcos["ID"][i], dataArcos["Distancia"][i], str(dataArcos["Nombre"][i]))

for e in Nodes:
    print(e)
