#! /usr/env/python

def print_all_paths_helper(root, target):
    if not root:
        return 0
    return int(root.val == target) + print_all_paths_helper(root.left, target-root.val) + print_all_paths_helper(root.right, target-root.val)
def print_all_paths(root, sum):
    if not root:
        return 0

    return print_all_paths_helper(root, sum) + print_all_paths(root.left, sum) + print_all_paths(root.right, sum)