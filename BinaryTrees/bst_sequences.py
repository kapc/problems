#! /usr/env/python

"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input:
Output: {2, 1, 3}, {2, 3, 1}
Hints: #39, #48, #66, #82
110 Cracking
"""

class Node(object):
    """
    Node object.
    """
    def __init__(self, value):
        self._val = value
        self.right = None
        self.left = None

class BST(object):
    """
    BST object.
    """

    def __init__(self, input_arr):
        """
        :param input_arr:
        """
        self._root = self.build_bst(input_arr)

    def _build_bst_helper(self, arr, start, end):
        """
        :param arr:
        :param start:
        :param end:
        :return:
        """
        if start > end:
            return None

        mid = start + int((end - start) / 2)

        cur_val = arr[mid]
        root = Node(cur_val)

        root.left = self._build_bst_helper(arr, start, mid - 1)
        root.right = self._build_bst_helper(arr, mid + 1, end)

        return root

    def build_bst(self, input_arr):
        """

        :param input_arr:
        :return:
        """
        return self._build_bst_helper(input_arr, 0, len(input_arr) - 1)

    def _print_tree_helper(self, root):
        """

        :return:
        """
        if not root:
            return
        self._print_tree_helper(root.left)
        print(root._val)
        self._print_tree_helper(root.right)

    def print_tree(self):
        """

        :return:
        """
        self._print_tree_helper(self._root)
        print("===========================")

    def _height_tree_helper(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return 0

        return max(self._height_tree_helper(root.left),
                   self._height_tree_helper(root.right)) + 1

    def insert_node_helper(self, root, new_node):
        """

        :param root:
        :param new_node:
        :return:
        """
        if root is None:
            return new_node

        if new_node._val <= root._val:
            root.left = self.insert_node_helper(root.left, new_node)
        else:
            root.right = self.insert_node_helper(root.right, new_node)
        return root

    def _get_inorder_successor(self, root):
        """

        :param root:
        :return:
        """
        cur = root
        while cur.left is not None:
            cur = cur.left
        return cur

    def _delete_node_helper(self, root, value):
        """

        :param root:
        :param value:
        :return:
        """
        if not root:
            return None

        if value < root._val:
            root.left = self._delete_node_helper(root.left, value)
        elif value > root._val:
            root.right = self._delete_node_helper(root.right, value)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self._get_inorder_successor(root.right)
                root.right = self._delete_node_helper(root.right, successor._val)
                root._val = successor._val

        return root

    def delete_node(self, value):
        """

        :param value:
        :return:
        """
        self._root = self._delete_node_helper(self._root, value)

    def insert_node(self, value):
        """

        :param value:
        :return:
        """
        new_node = Node(value)
        self._root = self.insert_node_helper(self._root, new_node)

    def height_tree(self):
        """

        :return:
        """
        return self._height_tree_helper(self._root)

    def _check_if_bst_helper(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return True
        if root.left:
            valid = root._val >= root.left._val and self._check_if_bst_helper(root.left)
            if not valid:
                return False
        if root.right:
            valid = root._val < root.right._val and self._check_if_bst_helper(root.right)
            if not valid:
                return True
        return True

    def _check_if_bst_smart(self, root, max_left, min_right):
        """

        :return:
        """
        if not root:
            return True


        balanced = root._val <= max_left and root._val >= min_right
        return (balanced and
                self._check_if_bst_smart(root.left, root._val, min_right) and
                self._check_if_bst_smart(root.right, max_left, root._val))

    def check_if_bst(self):
        """

        :return:
        """
        max_int = sys.maxint
        min_int = -sys.maxint + 1
        return self._check_if_bst_helper(self._root) and self._check_if_bst_smart(self._root, max_int, min_int)

    def _get_result_array(self, root, result):
        """

        :return:
        """
        if not root:
            return
        self._get_result_array(root.left, result)
        result.append(root._val)
        self._get_result_array(root.right, result)

    def return_result_array(self):
        """
        :return:
        """
        result = []
        self._get_result_array(self._root, result)
        return result

    def print_all_leaves_helper(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return

        if root.left is None and root.right is None:
            print(root._val)
            return
        self.print_all_leaves_helper(root.left)
        self.print_all_leaves_helper(root.right)

    def print_all_leaves(self):
        """

        :return:
        """
        self.print_all_leaves_helper(self._root)

    def _is_balanced_helper(self, root):
        """

        :param left_height:
        :param right_height:
        :return:
        """
        if not root:
            return True

        left_height = self._height_tree_helper(root.left)
        right_height = self._height_tree_helper(root.right)

        return (abs(left_height - right_height) < 2
                and self._is_balanced_helper(root.left)
                and self._is_balanced_helper(root.right))

    def _is_balanced_smart(self, root):
        """

        :param root:
        :param left_height:
        :param right_height:
        :return:
        """
        if not root:
            return -1
        height_left = self._is_balanced_smart(root.left)
        height_right = self._is_balanced_smart(root.right)

        if height_right == -1 or height_left == -1:
            return -1
        if abs(height_left - height_right) > 1:
            return -1

        return max(height_left, height_right) + 1

    def is_balanced(self):
        """

        :return:
        """
        return self._is_balanced_smart(self._root)

    def bst_sequences(self):
        """

        :return:
        """
        


arr = [1,2,3,4]
b = BST(arr)
b.print_tree()