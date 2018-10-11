#! /usr/env/python

"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
Hints: #127
"""

class Graph:
    def __init__(self):
        self.nodes = []

class Node:
    def __init__(self, value):
        print("Created {}".format(value))
        self.value = value
        self.children = []

def BFS(source_node):
    q = [source_node]
    visited = []
    while q:
        cur_node = q.pop(0)
        if cur_node in visited:
            continue
        print(cur_node.value)
        visited.append(cur_node)
        q.extend(cur_node.children)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n0 = Node(0)
n4 = Node(4)

n1.children += [n2]
n2.children += [n0, n3]
n3.children += [n2]
n0.children += [n1]

BFS(n1)

