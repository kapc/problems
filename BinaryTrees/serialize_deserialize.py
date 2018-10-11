#! /usr/env/python

"""
https://leetcode.com/problems/serialize-and-deserialize-bst/description/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


class Codec:

    def serialize_helper(self, root, result_str):
        """
        Serialize a tree.
        """
        if root is None:
            result_str.append("#")
            return None

        val = root.val
        result_str.append(str(val))
        root.left = self.serialize_helper(root.left, result_str)
        root.right = self.serialize_helper(root.right, result_str)

        return root

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result_str = []
        self.serialize_helper(root, result_str)
        return "".join(result_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        index = [0]

        def deserialize_helper(data):
            """
            """
            if index[0] >= len(data):
                return None
            if data[index[0]] == "#":
                index[0] += 1
                return None
            root = TreeNode(data[index[0]])
            index[0] += 1
            root.left = deserialize_helper(data)
            root.right = deserialize_helper(data)
            return root

        return deserialize_helper(data)