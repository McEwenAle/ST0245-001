import numpy as np

class Image:
    def __init__(self, d) -> None:
        self.d = d
        self.importPhoto()

    def importPhoto(self):
        file = open(self.d)
        self.photo = np.loadtxt(file, delimiter=",")
    
    def export(self, d):
        np.savetxt(d, self.photo, delimiter=",")

    def compressByFactor(self, factor):
        self.compress(self.photo, len(self.photo)/factor, len(self.photo)/factor)

    def amplifyByFactor(self, factor):
        self.amplify(self.photo, len(self.photo)/factor, len(self.photo)/factor)

    def compress(self, n, m):
        if len(self.photo) <= n or len(self.photo[0]) <= m:
            return self.photo
        cF1 = len(self.photo) / n
        cF2 = len(self.photo[0]) / m
        if cF1 != cF2 and int(cF1) != cF1:
            return self.photo
        cF = int(cF1)
        new_self.photo = np.ndarray((n,m))
        for i in range(n):
            for j in range(m):
                new_self.photo[i][j] = int(self.photo[int(cF*i+int(cF/2))][int(cF*j+int(cF/2))])
        self.photo = new_self.photo.astype(int)
    #Decompress
    def amplify(self, n, m):
        if len(self.photo) >= n or len(self.photo[0]) >= m:
            return self.photo
        cF1 =  n / len(self.photo)
        cF2 =  m / len(self.photo[0])
        if cF1 != cF2 and int(cF1) != cF1:
            return self.photo
        cF = cF1
        new_self.photo = np.ndarray((n,m))
        k = -1
        l = -1
        for i in range(n):
            if i % cF == 0:
                k+=1
            l = -1
            for j in range(m):
                if j % cF == 0:
                    l+=1
                new_self.photo[i][j] = self.photo[k][l]
        self.photo = new_self.photo.astype(int)






