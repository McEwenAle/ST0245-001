import math
import numpy as np
import pandas as pd
import os, sys


ganadoEnfermoCSVs = "./archivosCSV/ganadoEnfermoCSVs"
ganadoSanoCSVs = "./archivosCSV/ganadoSanoCSVs"

dirGanadoEnfermoCSVs = os.listdir(ganadoEnfermoCSVs)

dirGanadoSanoCSVs = os.listdir(ganadoSanoCSVs)

dataGanadoEnfermoCSVs = [[]] * len(dirGanadoEnfermoCSVs)
dataGanadoSanoCSVs = [[]] * len(dirGanadoSanoCSVs)

for i in range(len(dirGanadoEnfermoCSVs)):
    p = ganadoEnfermoCSVs + "/" + dirGanadoEnfermoCSVs[i]
    dataGanadoEnfermoCSVs[i] = pd.read_csv(p)

for i in range(len(dirGanadoSanoCSVs)):
    p = ganadoSanoCSVs + "/" + dirGanadoSanoCSVs[i]
    dataGanadoSanoCSVs[i] = pd.read_csv(p)

print(dataGanadoEnfermoCSVs)
print("############")
print(dataGanadoSanoCSVs)


