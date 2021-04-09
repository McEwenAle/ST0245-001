import numpy as np

class HashTable():
    
    def __init__(self):
        self.hashTable = np.full((1000000), -1, dtype = int)

    def funcion_hash(self, k):
        key = 0
        for i in range(len(k)):
            key += ord(k[i])*(i+1)
        return key

    def get(self, k):
        key = self.funcion_hash(k)
        val = self.hashTable[key]
        if val == -1:
            return None
        else:
            return val

    def put(self, k, v):       
        key = self.funcion_hash(k)
        self.hashTable[key] = v

# hashTable = HashTable()
# hashTable.put("Felipe", 13539432)
# hashTable.put("Alejandro", 18497294)
# print(hashTable.get("Felipe"))
# print(hashTable.get("Alejandro"))
# print(hashTable.get("Mauricio"))

hT = dict()
hT["Google"]= "Estados Unidos"
hT["La locura"] = "Colombia"
hT["Nokia"] = "Finlandia"
hT["Sony"] = "Japon"

def searchKey(dic, key):
    if key in dic:
        return dic[key]
    else:
        return None
    
print(searchKey(hT, "Google"))
print(searchKey(hT, "Motorola"))

def searchValue(dic, v):
    l = []
    for e in dic.keys():
        if dic[e] == v:
            l.append(e)
    return l

hT["Apple"] = "Estados Unidos"

print(searchValue(hT, "Estados Unidos"))