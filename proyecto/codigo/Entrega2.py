import numpy as np

class Compresor:
    def __init__(self) -> None:
        pass

    def compressByFactor(self, photo, factor):
        self.compress(photo, len(photo)/factor, len(photo)/factor)

    def amplifyByFactor(self, photo, factor):
        self.amplify(photo, len(photo)/factor, len(photo)/factor)

    def compress(self, photo, n, m):
        if len(photo) <= n or len(photo[0]) <= m:
            return photo
        cF1 = len(photo) / n
        cF2 = len(photo[0]) / m
        if cF1 != cF2 and int(cF1) != cF1:
            return photo
        cF = int(cF1)
        new_photo = np.ndarray((n,m))
        for i in range(n):
            for j in range(m):
                new_photo[i][j] = int(photo[int(cF*i+int(cF/2))][int(cF*j+int(cF/2))])
        return new_photo.astype(int)
    #Decompress
    def amplify(self, photo, n, m):
        if len(photo) >= n or len(photo[0]) >= m:
            return photo
        cF1 =  n / len(photo)
        cF2 =  m / len(photo[0])
        if cF1 != cF2 and int(cF1) != cF1:
            return photo
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
                new_photo[i][j] = photo[k][l]
        return new_photo.astype(int)






