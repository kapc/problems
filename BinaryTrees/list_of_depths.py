#! /usr/env/python

"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you 'll have D linked lists).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = LinkedNode(value)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next
        print("=================")

def list_of_depths(root):
    result = []

    if not root:
        return result
    q = [(root, 0)]
    prev_level = 0
    l = LinkedList()
    cur_list = []

    while q:
        cur_node, cur_level = q.pop(0)
        if prev_level != cur_level:
            result.append(l)
            l = LinkedList()
        l.add_node(cur_node.value)
        if cur_node.left:
            q.append((cur_node.left, cur_level + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_level + 1))
        prev_level = cur_level
    result.append(l)

    for l in result:
        l.print_list()

    return result


def generate_minimal_tree_helper(arr_list, left, right):
    """

    :param arr_list:
    :param left:
    :param right:
    :return:
    """
    if left > right:
        return None
    mid = left + int((right - left) / 2)
    value = arr_list[mid]
    cur_node = Node(value)
    cur_node.left = generate_minimal_tree_helper(arr_list, left, mid - 1)
    cur_node.right = generate_minimal_tree_helper(arr_list, mid + 1, right)

    return cur_node

def pre_order(root):
    if not root:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)

def height_tree(root):
    if not root:
        return 0
    return 1 + max(height_tree(root.left), height_tree(root.right))

def generate_minimal_tree(arr_list):
    left = 0
    right = len(arr_list) - 1
    return generate_minimal_tree_helper(arr_list, left, right)

arr_list = [1,2,3,4,5,6,7,8,9,10]
root = generate_minimal_tree(arr_list)
result = list_of_depths(root)
print(result)