import numpy as np

class Hash3D:

    def __init__(self):
        arr = np.full([2000, 2000, 2000], [])
    
    def hashfunction(self, x, y, z):
        return (x//100, y//100, z//100)

    def add(self, x, y, z):
        h = self.hashfunction(x, y, z)
        self.arr[h[0]][h[1]][h[2]].append((x, y, z))

    def searchPerimeter(self, x, y, z):
        nx = x/100
        ny = y/100
        nz = z/100
        l = [[], [], []]
        nv = [nx, ny, nz]
        for i in range(3):
            if nv[i] == int(nv[i]):
                l[i].append(int(nv[i]))
            else:
                l[i].append(floor(nv[i]))
                l[i].append(ceil(nv[i]))


    def combinations(self, l):
        ll = []
        i, j, k = 0, 0, 0
        while i != len(l[0]):
            ll.append((l[0][i], l[1][j], l[2][k]))
            k += 1
            if k == len(l[2]):
                k = 0
                j += 1
            if j == len(l[1]):
                j = 0
                i += 1
        return ll


            
        