import numpy as np
import math

class Hash3D:

    def __init__(self):
        self.arr = [[[[] for i in range(100)] for j in range(100)] for k in range(100)]
    
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
            l[i].append(math.floor(nv[i]))
            l[i].append(math.floor(nv[i]) + 1)
            l[i].append(math.floor(nv[i]) - 1)
        ll = self.combinations(l)
        ans = []
        for x1, y1, z1 in ll:
            for x2, y2, z2 in self.arr[x1][y1][z1]:
                print(x1, y1, z1)
                print(x2, y2, z2)
                if math.sqrt(pow(x2-x,2) + pow(y2-y,2) + pow(z2-z,2)) <= 100:
                    ans.append((x2, y2, z2))
        return ans
        

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

hA = Hash3D()
hA.add(0,0,0)
hA.add(100,0,0)
hA.add(200, 100, 300)
print(hA.searchPerimeter(100,0,0))
