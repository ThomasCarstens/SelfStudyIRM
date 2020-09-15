import numpy as np
import math
import test
import matplotlib.pyplot as plt

def iterative(number_of_terms):

    counter = 0

    first = 0
    second = 1
    temp = 0

    while counter <= number_of_terms:
        print(first)
        temp= first+second
        first = second
        second = temp
        counter = counter+1
#Driver Code
iterative(10)

def fib(term):
    if term <=1:
        return (term)
    else:
        return (fib(term-1)+fib(term-2))
number_of_terms= 10
for i in range(number_of_terms):
    print(fib(i))
