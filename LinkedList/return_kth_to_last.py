# /usr/env/python

"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
Hints: #8, #25, #47, #67, # 726
"""

"""
1-2-3-4
2nd to last = 2
3rd to last = 2
5th to last = None
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self._head = None
        self._node_dict = {}

    def add_node(self, new_node):
        if not self._head:
            self._head = new_node
            return
        new_node.next = self._head
        self._head = new_node

    def return_kth_to_last(self, k):
        ptr1 = self._head
        ptr2 = self._head
        count = 0
        while count < k and ptr2:
            ptr2 = ptr2.next
            count += 1
        if count < k:
            return None
        while ptr1 and ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1.val

    def print_list(self):
        cur = self._head
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    l = LinkedList()
    l.add_node(Node(1))
    l.add_node(Node(2))
    l.add_node(Node(3))
    l.add_node(Node(4))
    l.add_node(Node(5))
    l.add_node(Node(6))

    print(l.return_kth_to_last(8))

