import functools
import time
import numpy as np

class Image:
    def __init__(self, d) -> None:
        self.d = d
        self.importPhoto()

    def importPhoto(self):
        file = open(self.d)
        self.photo = np.loadtxt(file, delimiter=",").astype(np.intc)
        self.rows = len(self.photo)
        self.cols = len(self.photo[0])
    
    def export(self, d):
        a_file = open(d, "w")
        for row in self.photo:
            np.savetxt(a_file, row, newline=',', fmt='%d')
            a_file.write("\n")
        a_file.close()

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

    def losslessCompress(self):
        print(len(self.photo), len(self.photo[0]))
        startTime = time.time()
        icp = []
        count = 1
        k = 1
        while k < len(self.photo) * len(self.photo[0]):
            i = k // len(self.photo[0])
            j = k % len(self.photo[0])
            i1 = (k-1) // len(self.photo[0])
            j1 = (k-1) % len(self.photo[0])
            if self.photo[i][j] == self.photo[i1][j1]:
                count += 1
            else:
                if count == 1:
                    icp.append([self.photo[i1][j1]])
                else:
                    icp.append([self.photo[i1][j1], count])
                count = 1
            k += 1
        self.photo = np.array(icp)
        print(len(self.photo), len(self.photo[0]))
        endtime = time.time()
        print(endtime - startTime)

    # def losslessCompress(self):
    #     startTime = time.time()
    #     print(len(self.photo), len(self.photo[0]))
    #     prefix = 2000
    #     k = 0
    #     icp = []
    #     while k < len(self.photo) * len(self.photo[0]):
    #         i = k // len(self.photo[0])
    #         j = k % len(self.photo[0])
    #         t = [self.photo[i][j], 0, 0]
    #         for k1 in range(k - 1 , max(k - prefix, -1), -1):
    #             i = k // len(self.photo[0])
    #             j = k % len(self.photo[0])
    #             i1 = k1 // len(self.photo[0])
    #             j1 = k1 % len(self.photo[0])
    #             if self.photo[i][j] == self.photo[i1][j1]:
    #                 c = 1
    #                 for n in range(1, min(prefix, len(self.photo) * len(self.photo[0]) - k)):
    #                     i = (k+n) // len(self.photo[0])
    #                     j = (k+n) % len(self.photo[0])
    #                     i1 = (k1+n) // len(self.photo[0])
    #                     j1 = (k1+n) % len(self.photo[0])
    #                     c = n
    #                     if self.photo[i][j] != self.photo[i1][j1]:
    #                         break
    #                 i = (k+c) // len(self.photo[0])
    #                 j = (k+c) % len(self.photo[0])
    #                 if  k + 1 < len(self.photo) * len(self.photo[0]) and t[2] < c:
    #                     t = [self.photo[i][j], k - k1, c]
    #         if t[2] < 2:
    #             t = [self.photo[i][j]]
    #         else:
    #             k += t[2]
    #         k += 1
    #         icp.append(t)
    #     self.photo = np.array(icp)
    #     endtime = time.time()
    #     print(len(self.photo), len(self.photo[0]))
    #     print(endtime - startTime)


    def losslessDecompress(self):
        idp = [[0]*self.cols for _ in range(self.rows)]
        k = 0
        for l in range(len(self.photo)):
            i = k // self.cols
            j = k % self.cols
            if len(self.photo[l]) == 1:
                idp[i][j] = self.photo[l][0]
                k += 1
            else:
                for n in range(self.photo[l][2]):
                    i = (k + n) // self.cols
                    j = (k + n) % self.cols
                    i1 = (k - self.photo[l][1] + n) // self.cols
                    j1 = (k - self.photo[l][1] + n) % self.cols
                    idp[i][j] = idp[i1][j1]
                k += self.photo[l][2]
                i = k // self.cols
                j = k % self.cols
                idp[i][j] = self.photo[l][0]
                k += 1
        self.photo = idp
