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
        self.__elements[size] = object
        self.__size+=1

    def addInIndex(self, index, object):
        if self.__size == self.__realSize:
            self.__elements = np.array(self.__elements + [0]*self.__realSize)
            self.__realSize*=2 
        self.__size+=1
        temp = self.__elements[index]
        for i in range(index, size):
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
        self.__elements[size] = 0
    
    def removeInIndex(self, index):
        temp2 = 0
        self.__size-=1
        for i in range(size, index-1, -1):
            if abs(i - size)%2 == 0:
                temp = self.__elements[i]
                self.__elements[i] = temp2
            else:
                temp2 = self.__elements[i]
                self.__elements[i] = temp

arr = new ArrayList()
arr.add(23)
print arr