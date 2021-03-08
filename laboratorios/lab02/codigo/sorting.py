import random
import time

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

def combine(arr, arr2):
    nArr = []
    if arr[len(arr) - 1]  <= arr2[0]:
        for e in arr:
            nArr.append(e)
        for e in arr2:
            nArr.append(e)
    elif arr[0]  >= arr2[len(arr2) - 1]:
        for e in arr2:
            nArr.append(e)
        for e in arr:
            nArr.append(e)
    else:
        i = 0
        j = 0
        while i < len(arr) and j < len(arr2):
            if arr[i] < arr2[j]:
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


def merge_sort(arr):
    l = []
    split(arr, l)
    for e in l:
        if len(e) != 1 and e[0] > e[1]:
            swap(e, 0, 1)
    while len(l) !=  1:
        a = l.pop()
        b = l.pop()
        aB = combine(a, b)
        l.insert(0, aB)
    return l[0]

# arr = [2,1,4,3,5,6]
# sarr = merge_sort(arr)
# print(sarr)
for i in range(1, 22):
    arr = []
    for j in range(i*1000):
        arr.append(int(random.random()*i))
    start = time.time()
    insertionSort(arr)
    print(time.time() - start)