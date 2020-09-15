import numpy as np
import math
import test
import matplotlib.pyplot as plt


##STACK USING A LIST
class Stack:
    def __init__(self, stack):
        self.stack = stack
#add, pop, size:
    def add(self, new):
        self.stack.append(new)
        return stack

    def pop(self, old):
        if self.stack.__len__() != 0:
            self.stack.pop()
            return stack
        else:
            "Can't pop: No elements."

    def size(self):
        size = self.stack.__len__()
        print("size: ", size)
        return size

stack1 = Stack([])
stack1.pop()
string="((()))"
#program to check if a given str has balanced parenthesis
#balanced if final stack is empty.

#first iterate through string:
    # if string.split[0]=="(":
        #stack.append();
