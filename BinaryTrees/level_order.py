#! /usr/env/python


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [(root, 0)]
        depth = 0
        cur_depth = 0
        l = []
        result = []
        for node, depth in queue:
            if node:
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    result.insert(0, l)
                    l = []
                l.append(node.val)
        if l:
            result.insert(0, l)
        return result
