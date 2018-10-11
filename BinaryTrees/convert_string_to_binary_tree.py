#! /usr/env/python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
"""

class Solution(object):
    def get_next_val(self, s, idx):
        val = ""
        while idx < len(s) and s[idx] != ")" and s[idx] != "(":
            val += s[idx]
            idx += 1
        return str(val), idx

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        val, idx = self.get_next_val(s, 0)
        root = TreeNode(val)
        stack_nodes = [root]
        while idx < len(s):
            cur_char = s[idx]
            if cur_char == "(":
                if idx + 1 >= len(s):
                    assert False, "Invalid string."
                val, idx = self.get_next_val(s, idx + 1)
                new_node = TreeNode(val)
                cur_node = stack_nodes[-1]
                if cur_node.left is None:
                    cur_node.left = new_node
                else:
                    cur_node.right = new_node
                stack_nodes.append(new_node)
            elif cur_char == ")":
                cur_node = stack_nodes.pop()
                idx += 1
            else:
                assert False, "Invalid String"
        return root