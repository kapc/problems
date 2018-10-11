#! /usr/env/python

"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def check_if_balanced(root):
    if root is None:
        return 0, True

    height_left, balanced_left = check_if_balanced(root.left)
    height_right, balanced_right = check_if_balanced(root.right)

    if not balanced_left or not balanced_right:
        return -1, False

    if abs(height_left - height_right) > 1:
        return -1, False

    return max(height_left, height_right) + 1, True

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

height_val, balanced = check_if_balanced(root)
print(height_val, balanced)
