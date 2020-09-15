import numpy as np
import math
import test
import matplotlib.pyplot as plt

##STACK USING A LIST
class Array:
    def __init__(self, array):
        self.array = array
#add, pop, size:
    def add(self, new):
        self.array.append(new)
        return stack

    def pop(self):
        if self.array.__len__() != 0:
            self.array.pop()
            return stack
        else:
            "Can't pop: No elements."

    def size(self):
        size = self.array.__len__()
        print("size: ", size)
        return size

    def min(self):
        min = self.array[0]
        print(self.array[0])
        for i in range(self.array.__len__()):
            print (i)
            if self.array[i]< min:
                min = self.array[i]
        print ("min:",min)
        return min

    def duplicates(self):
        #do later
        print("#TODO")
        #list array[i] against array [j]
        #find equal versions that are not in same position i==j.
        #assume only one ie. return(?)

    def move_zeroes(self):
        #first find a zero,
        #then item.remove()
        #then item.append() at end i= array length.
        print("#TODO")


    def mergesort(self, l, m, r):
        #FROM https://www.geeksforgeeks.org/python-program-for-merge-sort/
        #MUST BE VERIFIED.
        #first merge two arrays, array1[l:m] and array2[m+1:r]
        n1 = m - l + 1
        n2 = n - m
        #temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range (0, n2):
            R[j] = arr[m + 1 +j]

        i=0
        j=0
        k=l

        while i<n1 and j<n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j +=1
            k +=1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while i < n2:
            arr[k] = R[j]
            i += 1
            k += 1
    ## A VERIFIER.
    def mergeSort(arr, l, r):
        if l<r:
            m=(l+(r-1))//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)

    def i_of_min(self, min):
        index = -1;
        print("transfer min:", min)
        for i in range(self.array.__len__()):
            print (i)
            if self.array[i] == min:
                index = i
                print("the value: ", self.array[i])
                print("its index:", index)
                return index


a1 = Array([3,2,5,3,1])
#a1.min()
a1.i_of_min(a1.min())
