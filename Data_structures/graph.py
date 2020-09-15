import numpy as np
import math
import test
import matplotlib.pyplot as plt
from collections import deque

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
##file:///home/txa/SelfStudyIRM/Data%20Structure%20and%20Algorithms%20--%20Ouch.pdf
##COMPLEXITY: https://www.datacamp.com/community/tutorials/analyzing-complexity-code-python
##COMPLEXITY: https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
##COMP: BASICS https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
##DIFF. FIB SEQ https://www.educative.io/edpresso/how-to-implement-the-fibonacci-sequence-in-python

##Adapted from: https://www.python.org/doc/essays/graphs/
#function to find a path between two nodes: return a list of nodes comprising the path.
def find_path(graph, start, end, path=[]): #path default not traversed
    path = path + [start]  #creates a new list.
    if start == end:
        return path #avoiding cycles.
    if not start in graph: #if no path is found.
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]): #path default not traversed
    path = path + [start]  #creates a new list.
    if start == end:
        return [path] #avoiding cycles.
    if not start in graph: #if no path is found.
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]): #path default not traversed
    path = path + [start]  #creates a new list.
    if start == end:
        return path #MUST FIND SHORTEST
    if not start in graph: #if no path is found.
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath)<len(shortest):
                    shortest = newpath
    return shortest

def bfs_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)
 ##LIST THE EDGES
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    #print(edges)
    return edges

print(generate_edges(graph))
#sample run:
print(find_path(graph, 'A', 'D'))
print(find_all_paths(graph, 'A', 'D'))
print(find_shortest_path(graph, 'A', 'D'))
print(bfs_shortest_path(graph, 'A', 'D'))

class Node:
    def __init__(self, id):
        self.id = id #id per node.
        self.connections = []

    def print_connections(self):
        for conn in self.connections:
            print(f'{self.id}->{conn.id}')
class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def is_connected(self, n1: Node, n2: Node):
        for conn in self.connections:
            if n1 in conn and n2 in conn:
                return True
        return False

    def connect(self, n1: Node, n2: Node):
        self.connections.append([n1, n2])

    #def disconnect()...
#more adapted from https://www.python-course.eu/graphs_python.php

import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
nx.shortest_path(G, 'A', 'D', weight='weight')

nx.draw(G, with_labels=True, font_weight='bold')
#nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()
