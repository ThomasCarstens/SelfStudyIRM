import numpy as np
import math
import test
import matplotlib.pyplot as plt


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def L2_norm(self):
        return math.sqrt(self.x**2+self.y**2)

    def __mul__(self, c):
        v3 = Vec2(self.x*c, self.y*c)
        # v3.x = self.x * c
        # v3.y = self.y * c
        print(v3.x)
        return v3
        #By Scalar
        #return self.x *c, self.y *c

    def mul_vec(self, other):
        v3 = Vec2(self.x*other.x, self.y*other.y)
        # v3.x = self.x * c
        # v3.y = self.y * c
        print("mul w/new: ", v3)
        return v3
        #By Scalar
        #return self.x *c, self.y *c

    def __str__(self):
        return (str)(self.x) + ", " + (str)(self.y)

    def subtract(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return v1.x, v1.y

    def add (self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        print("add w/same: ", v1)
        return v1.x, v1.y

# v1 = Vec2(1,2)
# v2 = Vec2(2,4)
#
# # print(v1.x, v1.y)
# # print(v1.L2_norm())
# print (v1*3)
# ###print (v1*v2)
# # print(v1.x, v1.y)

class Referential:
    def __init__(self, ref):
        self.x= ref[0]
        self.y = ref[1]

class BasedVec2(Vec2):
    def __init__(self, x, y, ref):
        ##super(BasedVec2, self).__init__(x, y)
        self.x = x
        self.y = y
        self.ref = ref

    def translate(self, other):
        if other.ref != self.ref:
            print ("Manual Halt: not same base.")
        else:
            out = self.add(other)
            print(out)
            return self.add(other)

    def mul(self):
        print (1)
        return self.mul_vec(self.ref)

# b_v1 = BasedVec2(1,2,1)
# print(b_v1.translate())
# #NEW REFERENTIELS
# referentiel1 = Referential([1,1])
# referentiel0 = Referential([0,0])
# b_v1 = BasedVec2(1,2,referentiel1)
# print(b_v1.mul())
# b_v2 = BasedVec2(1,2,referentiel0)
# b_v1.translate(b_v2)
#########################################3
##MATPLOTLIB
# def intervalles():
#     #https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
#     evenly=np.linspace(0, 100)
#     print(evenly)
# intervalles()
#
# def graph():
#     for i in range (100):
#         x1 = i
#         y1=2*x1
#         plt.plot(x1, y1, 'bo')
#         plt.show()
# graph()

#FROM SCRATCH
# point1 = [1, 2]
# point2 = [3, 4]
# point3 = [5, 6]
# point4 = [7, 8]
# x_values = [point1[0], point2[0]]
# #gather x-values
# y_values = [point1[1], point2[1]]
# #gather y-values
# plt.plot(x_values, y_values)
# # plt.plot([1,2], [2,3])
# plt.show()

#USING A class
class Shape:
    def __init__(self, point_list):
        ##super(BasedVec2, self).__init__(x, y)
        self.point_list = point_list
        self.x=[]
        self.y=[]
        for pt in point_list:
            self.x.append(pt[0])
            self.y.append(pt[1])
        print(self.x)

    def accept(self, line):
        #accept new lines
        None

    def display(self):
        #How to plot: take all x's and y's.
        plt.plot(self.x, self.y)
        plt.show()
        #show point_list.
        None

def firstgraph():
    pts = [[0,1],[2,1]]
    newshape = Shape(pts)
    newshape.display()

# 1.Write a program that calculates the sum of a list, using recursion
# 2.Using recursion, write a program that converts any integer to a string
# in a basebetween 2 and 9
# 3.Write a program, using recursion to sum
# all the elements of a list even with in-depthlists
# (Example f([1, [1, 2], [[1], [2,3]]) = 10)
# 4.Write a recursive to put a number to a certain power
