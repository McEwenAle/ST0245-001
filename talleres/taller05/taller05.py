import time
import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if(arr[j] < arr[j-1]):
                swap(arr, j, j-1)
            else:
                break

# arr = [4,6,5,2,1,7,3,9,8]
# print(arr)
# insertionSort(arr)
# print(arr)

# for i in range(1, 22):
#     arr = []
#     for j in range(i*500):
#         arr.append(int(random.random()*i))
#     start = time.time()
#     insertionSort(arr)
#     print(time.time() - start)

def sumArray(arr):
    s = 0
    for i in range(len(arr)):
        s += arr[i]
    return s

for i in range(1, 22):
    arr = []
    for j in range(i*1000000):
        arr.append(int(random.random()*i))
    start = time.time()
    sumArray(arr)
    print(time.time() - start)

def tablasDeMultiplicar(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # print(str(i)," * ", str(j), " = ", str(i*j))
            pass


# for i in range(1, 22):
#     start = time.time()
#     tablasDeMultiplicar(i*1000)
#     print(time.time() - start)
