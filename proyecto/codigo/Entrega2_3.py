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
        cF1 =  n / len(self.photo
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

    def cmpFunction(self, n, m):
        if self.photo[self.i][n] > self.photo[self.i][m]:
            return -1
        elif self.photo[self.i][n] < self.photo[self.i][m]:
            return 1
        else:
            return 0

    def losslessCompress(self):
        icp = []
        for i in range(len(self.photo)):
            index = []
            icp.append([])
            self.i = i
            for j in range(len(self.photo[i])):
                index.append(j)
            index = merge_sort(self.photo[i], index)
            for j in range(len(index)):
                index[j] -= 1
                if index[j] == -1:
                    index[j] = "|"
                else:
                    index[j] = self.photo[i][j] 
            count = 1
            for j in range(1, len(index)):
                if index[j] == index[j-1]:
                    count += 1
                else:
                    icp[i].append(index[j])
                    icp[i].append(count)
                    count = 1
        self.photo = np.array([np.array(x) for x in icp])

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def split(arr, l):
    if len(arr) <= 2:
        l.append(arr)
        return
    nArr = []
    nArr2 = []
    for i in range(int(len(arr)/2)):
        nArr.append(arr[i])
    for i in range(int(len(arr)/2), len(arr)):
        nArr2.append(arr[i])
    split(nArr, l)
    split(nArr2, l)

def combine(val, arr, arr2):
    nArr = []
    if val[arr[len(arr) - 1]]  <= val[arr2[0]]:
        for e in arr:
            nArr.append(e)
        for e in arr2:
            nArr.append(e)
    elif val[arr[0]]  >= val[arr2[len(arr2) - 1]]:
        for e in arr2:
            nArr.append(e)
        for e in arr:
            nArr.append(e)
    else:
        i = 0
        j = 0
        while i < len(arr) and j < len(arr2):
            if val[arr[i]] < val[arr2[j]]:
                nArr.append(arr[i])
                i +=  1
            else:
                nArr.append(arr2[j])
                j +=  1
        while i < len(arr):
            nArr.append(arr[i])
            i += 1
        while j < len(arr2):
            nArr.append(arr2[j])
            j += 1
    return nArr


def merge_sort(val, arr):
    l = []
    split(arr, l)
    for e in l:
        if len(e) != 1 and val[e[0]] > val[e[1]]:
            swap(e, 0, 1)
    while len(l) !=  1:
        a = l.pop()
        b = l.pop()
        aB = combine(val, a, b)
        l.insert(0, aB)
    return l[0]