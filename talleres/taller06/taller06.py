import numpy as np

class ArrayList:
    def __init__(self):
        self.__elements = np.array([0]*10)
        self.__size = 0
        self.__realSize = 10

    def size(self):
        return self.__size

    def get(self, index):
        return self.__elements[index]

    def add(self, object):
        if self.__size == self.__realSize:
            self.__elements = np.array(self.__elements + [0]*self.__realSize)
            self.__realSize*=2            
        self.__elements[self.__size] = object
        self.__size+=1

    #La complejidad de agregar abejas no da para un arreglo con millones de abejas porque tomaria segundos agregar varias abejas.
    #La complejidad de agregar n abejas es n^2 porque estamos haciendo n veces el algoritmo de agregar abejas que tiene complejidad O(n) porque mueve todo los arreglo después de i a la derecha 
    def addInIndex(self, index, object):
        if self.__size == self.__realSize:
            self.__elements = np.array(self.__elements + [0]*self.__realSize)
            self.__realSize*=2 
        if index > self.__size:
            self.__elements[self.__size]
        else:
            self.__size+=1
            temp = self.__elements[index]
            for i in range(index, self.__size):
                if i == index:
                    self.__elements[i] = object
                elif (i - index)%2 == 0:
                    temp = self.__elements[i]
                    self.__elements[i] = temp2
                else:
                    temp2 = self.__elements[i]
                    self.__elements[i] = temp
    def remove(self):
        self.__size-=1
        self.__elements[self.__size] = 0
    
    def removeInIndex(self, index):
        temp2 = 0
        self.__size-=1
        for i in range(self.__size, index-1, -1):
            if abs(i - self.__size)%2 == 0:
                temp = self.__elements[i]
                self.__elements[i] = temp2
            else:
                temp2 = self.__elements[i]
                self.__elements[i] = temp

    def __str__(self) -> str:
        return self.__elements.__str__()

# arr = ArrayList()
# arr.add(23)
# arr.add(24)
# arr.add(25)
# arr.addInIndex(1,22)
# arr.remove()
# arr.removeInIndex(1)
# print(arr)

#La complejidad del algoritmo es O(n) porque solo recorre el arreglo una vez.
def reverse(vec_dic):
    for i in range(int(len(vec_dic)/2)):
        temp = vec_dic[i]
        vec_dic[i] = vec_dic[len(vec_dic) - i - 1]
        vec_dic[len(vec_dic) - i - 1] = temp

# l = [int(x) for x in input().split()]
# reverse(l)
# print(l)

def vectorN(n):
    arr = []
    for i in range(n+1):
        for j in range(1,i+1):
            arr.append(j)
    return arr

# print(vectorN(5))



