#! /usr/env/python

import Queue

def BFS(adj_list):
    """

    :param adj_list:
    :return:
    """
    q = Queue.Queue()
    q.put(0)
    visited = []

    while not q.empty():
        elem = q.get()
        if elem in visited:
            continue
        print elem
        visited.append(elem)
        edge_list = adj_list[elem]
        for elem in edge_list:
            q.put(elem)
    print "=================="

def DFS(adj_list):
    """

    :param adj_list:
    :return:
    """
    s = []
    visited = []
    s.append(0)

    while s:
        elem = s.pop()
        if elem in visited:
            continue
        print elem
        visited.append(elem)
        edge_list = adj_list[elem]
        for elem in edge_list:
            s.append(elem)
    print "=================="


def add_edge(node1, node2, adj_list):
    """

    :param node1:
    :param node2:
    :param adj_list:
    :return:
    """
    if node1 in adj_list:
        adj_list[node1].append(node2)
    else:
        adj_list[node1] = [node2]

def build_adj_list():
    adj_list = {}

    add_edge(0, 1, adj_list)
    add_edge(0, 4, adj_list)
    add_edge(1, 0, adj_list)
    add_edge(1, 4, adj_list)
    add_edge(1, 3, adj_list)
    add_edge(1, 2, adj_list)
    add_edge(2, 1, adj_list)
    add_edge(2, 3, adj_list)
    add_edge(3, 1, adj_list)
    add_edge(3, 4, adj_list)
    add_edge(3, 2, adj_list)
    add_edge(4, 0, adj_list)
    add_edge(4, 1, adj_list)
    add_edge(4, 3, adj_list)
    return adj_list

adj_list = build_adj_list()
BFS(adj_list)
DFS(adj_list)
