import math
import numpy as np
import pandas as pd
import os, sys
from Entrega2 import Image

class ImportExport:
    def __init__(self) -> None:
        pass

    def importPhotos(self, n=-1, m = -1):
        

        ganadoEnfermoCSVs = "./archivosCSV/ganadoEnfermoCSVs"
        ganadoSanoCSVs = "./archivosCSV/ganadoSanoCSVs"

        dirGanadoEnfermoCSVs = os.listdir(ganadoEnfermoCSVs)

        dirGanadoSanoCSVs = os.listdir(ganadoSanoCSVs)

        self.dataGanadoEnfermoCSVs = [[]] * len(dirGanadoEnfermoCSVs)
        self.dataGanadoSanoCSVs = [[]] * len(dirGanadoSanoCSVs)
        if n == -1 or n > len(dirGanadoEnfermoCSVs):
            n = len(dirGanadoEnfermoCSVs)
        if m == -1 or m > len(dirGanadoSanoCSVs):
            m = len(dirGanadoSanoCSVs)
        for i in range(n):
            p = ganadoEnfermoCSVs + "/" + dirGanadoEnfermoCSVs[i]
            self.dataGanadoEnfermoCSVs[i] = Image(p)

        for i in range(m):
            p = ganadoSanoCSVs + "/" + dirGanadoSanoCSVs[i]
            self.dataGanadoSanoCSVs[i] = Image(p)
            
    def export(self):
        outputGanadoEnfermoCSVs = "./archivosCSV/outputGanadoEnfermoCSVs"
        outputGanadoSanoCSVs = "./archivosCSV/outputGanadoSanoCSVs"

        # for i in range(len(self.dataGanadoEnfermoCSVs)):
        #     p = outputGanadoEnfermoCSVs + "/" + dirGanadoEnfermoCSVs[i]
        #     self.dataGanadoEnfermoCSVs[i].export(p)

        # for i in range(len(dirGanadoSanoCSVs)):
        #     p = outputGanadoSanoCSVs + "/" + dirGanadoSanoCSVs[i]
        #     self.dataGanadoSanoCSVs[i].export(p)

    # print(self.dataGanadoEnfermoCSVs)
    # print("############")
    # print(self.dataGanadoSanoCSVs)


