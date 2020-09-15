import numpy as np
import math
import test
import matplotlib.pyplot as plt

##Tutorial from:
##https://realpython.com/linked-lists-python/

#Head: where the list starts
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        #slight change to quickly create linked lists
        #seems to connect nodes.
        if nodes is not None:
            node = Node (data = nodes.pop(0)) #pop off topmost
            self.head = node
            for elem in nodes: #connect the rest...
                node.next = Node(data=elem)
                node = node.next


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None: #validating that the current node is NOT None
            yield node
            node = node.next

    #ADDING NODE TO START
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        #traverse the whole list until reaching the end.
        #set the current_node as the last node on the list.
        #add the new node as the next value of that current_node.
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        
#INSERTING BETWEEN TWO NODES
#REMOVING A NODE.
#DOUBLY LINKED LISTS
#https://realpython.com/linked-lists-python/


#Each node in the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

# BASIC LINKED LIST ####
# llist= LinkedList()
# first_node = Node ("a")
#Using from-scratch method...
# llist.head = first_node
# print(llist)
# second_node = Node ("b")
# first_node.next = second_node
# print(llist)

llist= LinkedList(["a","b","c","d","e"])
print(llist)
llist.add_first(Node("pre"))
print(llist)
