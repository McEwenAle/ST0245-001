
class Hash3D:

    def __init__(self):
        arr = [0]*100000000
    
    def firsthash(self, a, b):
        return 5*(a + b)*(a + b + 1) + b
    
    def hashfunction(self, x, y, z):
        h = self.firsthash(x, y)
        return firsthash(h, z)
