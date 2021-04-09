import math
import numpy as np
import pandas as pd
import os, sys
from Entrega2 import Compresor

compresor = Compresor()

ganadoEnfermoCSVs = "./archivosCSV/ganadoEnfermoCSVs"
ganadoSanoCSVs = "./archivosCSV/ganadoSanoCSVs"

dirGanadoEnfermoCSVs = os.listdir(ganadoEnfermoCSVs)

dirGanadoSanoCSVs = os.listdir(ganadoSanoCSVs)

dataGanadoEnfermoCSVs = [[]] * len(dirGanadoEnfermoCSVs)
dataGanadoSanoCSVs = [[]] * len(dirGanadoSanoCSVs)

for i in range(len(dirGanadoEnfermoCSVs)):
    p = ganadoEnfermoCSVs + "/" + dirGanadoEnfermoCSVs[i]
    file = open(p)
    dataGanadoEnfermoCSVs[i] = np.loadtxt(file, delimiter=",")

for i in range(len(dirGanadoSanoCSVs)):
    p = ganadoSanoCSVs + "/" + dirGanadoSanoCSVs[i]
    file = open(p)
    dataGanadoSanoCSVs[i] = np.loadtxt(file, delimiter=",")

outputGanadoEnfermoCSVs = "./archivosCSV/outputGanadoEnfermoCSVs"
outputGanadoSanoCSVs = "./archivosCSV/outputGanadoSanoCSVs"

# for i in range(len(dataGanadoEnfermoCSVs)):
#     p = outputGanadoEnfermoCSVs + "/" + dirGanadoEnfermoCSVs[i]
#     np.savetxt(p, dataGanadoEnfermoCSVs[i], delimiter=",")

# for i in range(len(dirGanadoSanoCSVs)):
#     p = outputGanadoSanoCSVs + "/" + dirGanadoSanoCSVs[i]
#     np.savetxt(p, dataGanadoSanoCSVs[i], delimiter=",")

# print(dataGanadoEnfermoCSVs)
# print("############")
# print(dataGanadoSanoCSVs)


