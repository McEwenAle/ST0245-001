import random
from matplotlib import pyplot as pl
import time

# def array_generator(len):
#     """List generator"""
   

# def array_sum(array, sum = 0):
#     """Add the elements in the list"""
 

# def multiplication_tables(n):
#     for i in range(1,n + 1):
#         for j in range(1,n + 1):
#             print (str(i) + " * " + str(j) + " = " + str(i*j))
#         print ("--------------------")

# def insertion_sort(list):
  

def arrayMax(arr):
    return arrayMax_aux(arr, 0, 0)

def arrayMax_aux(arr, i, m):
    if(i == len(arr)):
        return m
    return arrayMax_aux(arr, i+1, max(m, arr[i]))

def formas(n):
    if n == 0:
        return 1
    a = 0
    if n>1:
        a = formas(n-2)

    return  a + formas(n-1)


print(formas(4))
   

#----------------------------Fibonacci---------------------------------#

def fib_r(n):                             #Fibonacci recursivo
    if(n == 0): return 0
    if(n <= 2): return 1
    return fib_r(n-1) + fib_r(n-2)

print(fib_r(4))
   

