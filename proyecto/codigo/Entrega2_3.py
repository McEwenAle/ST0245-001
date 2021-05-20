import functools
import numpy as np

class Image:
    def __init__(self, d) -> None:
        self.d = d
        self.importPhoto()

    def importPhoto(self):
        file = open(self.d)
        self.photo = np.loadtxt(file, delimiter=",").astype(np.intc)
    
    def export(self, d):
        np.savetxt(d, self.photo.astype(int), delimiter=",", fmt='%d')

    def lossyCompressByFactor(self, factor):
        self.lossyCompress(int(len(self.photo)/factor), int(len(self.photo[0])/factor))

    def amplifyByFactor(self, factor):
        self.amplify(int(len(self.photo)*factor), int(len(self.photo[0])*factor))

    def lossyCompress(self, n, m):
        if len(self.photo) <= n or len(self.photo[0]) <= m:
            return self.photo
        cF1 = len(self.photo) / n
        cF2 = len(self.photo[0]) / m
        if cF1 != cF2 and int(cF1) != cF1:
            return self.photo
        cF = int(cF1)
        new_photo = np.ndarray((n,m))
        for i in range(n):
            for j in range(m):
                new_photo[i][j] = int(self.photo[int(cF*i+int(cF/2))][int(cF*j+int(cF/2))])
        self.photo = new_photo.astype(np.intc)
    #Decompress
    def amplify(self, n, m):
        if len(self.photo) >= n or len(self.photo[0]) >= m:
            return self.photo
        cF1 =  n / len(self.photo)
        cF2 =  m / len(self.photo[0])
        if cF1 != cF2 and int(cF1) != cF1:
            return self.photo
        cF = cF1
        new_photo = np.ndarray((n,m))
        k = -1
        l = -1
        for i in range(n):
            if i % cF == 0:
                k+=1
            l = -1
            for j in range(m):
                if j % cF == 0:
                    l+=1
                new_photo[i][j] = int(self.photo[k][l])
        self.photo = new_photo.astype(np.intc)

    def keyFunction(self, item):
        i1 = item // len(self.photo[0])
        j1 = item % len(self.photo[0])
        return self.photo[i1][j1]

    def losslessCompress(self):
        icp = []
        index = []
        for i in range(len(self.photo)):
            for j in range(len(self.photo[i])):
                index.append(j+i*len(self.photo[i]))
        index = sorted(index, key=self.keyFunction)
        for k in range(len(index)):
            index[k] -= 1
            i1 = k // len(self.photo[0])
            j1 = k % len(self.photo[0])
            if index[k] == -1:
                index[k] = "|"
            else:
                index[k] = self.photo[i1][j1] 
        count = 1
        for k in range(1, len(index)):
            if index[k] == index[k-1]:
                count += 1
            else:
                icp.append(index[k-1])
                icp.append(count)
                count = 1
        print(icp)
        self.photo = np.array(icp)
    
    def losslessDecompress(self):
        idp = []
        for i in range(len(self.photo)):
            characters = []
            idp.append([])
            for j in range(0, len(self.photo[i]), 2):
                c = self.photo[i][j]
                n = self.photo[i][j+1]
                for k in range(n):
                    characters.append(c)

        table = [""] * len(r)  # Make empty table
        for i in range(len(r)):
            table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
        s = [row for row in table if row.endswith("\003")][0]  # Find the correct row (ending in ETX)
        return s.rstrip("\003").strip("\002")  # Get rid of start and end markers