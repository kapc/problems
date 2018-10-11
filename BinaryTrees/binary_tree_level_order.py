"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

1. Clarified the problem.
2. Checked corner cases.
3. Divised algorithm in brain.
4. Ran with few examples.
5. Wrote the final code.
6. Ran with more examples, including corner cases.
7. Discussed time and space complexity.
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if not root:
            return result

        node_list = [(root, 0)]
        last_level = 0
        cur_list = []

        while node_list:
            cur_node, cur_level = node_list.pop(0)
            if cur_level != last_level:
                result.append(cur_list)
                cur_list = []
                last_level = cur_level
            if cur_node.left:
                node_list.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                node_list.append((cur_node.right, cur_level + 1))
            cur_list.append(cur_node.val)
        if cur_list:
            result.append(cur_list)
        return result

"""
1. Clarified the problem. Input / Output
2. Corner cases.
3. Simple aglorithm.
4. Run with examples and corner cases.
5. Divise full algo in mind.
6. Write code now.
7. Test with examples.
8. Test with corner cases.
"""
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = {}
        if root is None:
            return []
        q = Queue.Queue()
        q.put((root, 0))

        while not q.empty():
            cur_node, cur_level = q.get()
            if cur_level in result:
                result[cur_level].append(cur_node.val)
            else:
                result[cur_level] = [cur_node.val]
            if cur_node.left:
                q.put((cur_node.left, cur_level - 1))
            if cur_node.right:
                q.put((cur_node.right, cur_level + 1))
        result = sorted(result.items(), key=lambda x: x[0])
        return [x[1] for x in result]