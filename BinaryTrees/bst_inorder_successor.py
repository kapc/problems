#! /usr/env/python

from create_bst_from_array import BST

class BSTSuccessor(BST):
    """
    Successor: Write an algorithm to find the "next" node (i .e., in-order successor) of a given node in a
    binary search tree. You may assume that each node has a link to its parent.
    """
    def __init__(self, input_arr):
        self._bst = BST(input_arr)


    def inorder_successor_helper(self, root, target, parent):
        """

        :param root:
        :param target:
        :return:
        """
        if not root:
            return None
        if target < root._val:
            return self.inorder_successor_helper(root.left, target, root)
        elif target > root._val:
            return self.inorder_successor_helper(root.right, target, parent)
        else:
            if root.right:
                cur = root.right
                while cur.left:
                    cur = cur.left
                return cur
        return parent

    def inorder_successor(self, target):
        """

        :return:
        """
        root = self._bst._root
        return self.inorder_successor_helper(root, target, None)


if __name__ == "__main__":
    input_arr = [11,22,32,44,55,66,77,88,99]
    bst_successor = BSTSuccessor(input_arr)

    target = 11
    result = [target]
    while True:
        node = bst_successor.inorder_successor(target)
        if not node:
            break
        result.append(node._val)
        target = node._val
    assert input_arr == result

