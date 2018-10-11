#! /usr/env/python

"""
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
Hints: #19, #73, #176
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

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
    print("Node is {}".format(root.value))
    pre_order(root.left)
    pre_order(root.right)

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
pre_order(root)
print(height_tree(root))