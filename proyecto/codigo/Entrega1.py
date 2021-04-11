import math
import numpy as np
import pandas as pd
import os, sys
from Entrega2 import Image

class ImageCompression:
    def __init__(self) -> None:
        pass

    def importPhotos(self, n=-1, m = -1):
        

        ganadoEnfermoCSVs = "./archivosCSV/ganadoEnfermoCSVs"
        ganadoSanoCSVs = "./archivosCSV/ganadoSanoCSVs"

        self.dirGanadoEnfermoCSVs = os.listdir(ganadoEnfermoCSVs)

        self.dirGanadoSanoCSVs = os.listdir(ganadoSanoCSVs)
        if n == -1 or n > len(self.dirGanadoEnfermoCSVs):
            n = len(self.dirGanadoEnfermoCSVs)
        if m == -1 or m > len(self.dirGanadoSanoCSVs):
            m = len(self.dirGanadoSanoCSVs)
        self.dataGanadoEnfermoCSVs = [[]] * n
        self.dataGanadoSanoCSVs = [[]] * m
        
        for i in range(n):
            p = ganadoEnfermoCSVs + "/" + self.dirGanadoEnfermoCSVs[i]
            self.dataGanadoEnfermoCSVs[i] = Image(p)

        for i in range(m):
            p = ganadoSanoCSVs + "/" + self.dirGanadoSanoCSVs[i]
            self.dataGanadoSanoCSVs[i] = Image(p)
    
    def compress(self, ratio):
        for e in self.dataGanadoEnfermoCSVs:
            e.compressByFactor(ratio)
        for e in self.dataGanadoSanoCSVs:
            e.compressByFactor(ratio)

    def amplify(self, ratio):
        for e in self.dataGanadoEnfermoCSVs:
            e.amplifyByFactor(ratio)
        for e in self.dataGanadoSanoCSVs:
            e.amplifyByFactor(ratio)

    def export(self):
        outputGanadoEnfermoCSVs = "./archivosCSV/outputGanadoEnfermoCSVs"
        outputGanadoSanoCSVs = "./archivosCSV/outputGanadoSanoCSVs"

        for i in range(len(self.dataGanadoEnfermoCSVs)):
            p = outputGanadoEnfermoCSVs + "/" + self.dirGanadoEnfermoCSVs[i]
            self.dataGanadoEnfermoCSVs[i].export(p)

        for i in range(len(self.dataGanadoSanoCSVs)):
            p = outputGanadoSanoCSVs + "/" + self.dirGanadoSanoCSVs[i]
            self.dataGanadoSanoCSVs[i].export(p)


