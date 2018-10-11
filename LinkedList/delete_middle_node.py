#! /usr/env/python

"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
"""

"""
1. We will be given reference to the new node.
2. a -> b -> c  a->c
3. a   None
4. a-> b -> c  d No change.

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

    def delete_middle_node(self, node):
        if not self._head or not node:
            return
        if self._head == node:
            self._head = self._head.next
            return
        cur = self._head
        prev = None
        while cur:
            if cur == node:
                assert prev is not None
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def get_nth_node(self, n):
        cur = self._head
        count = 0
        while count < n:
            cur = cur.next
            count += 1
        return cur

    def delete_middle_node_without_head(self, node):
        print("Deleting {}".format(node.val))
        if not node:
            return
        assert node.next is not None
        node.val = node.next.val
        next_node = node.next
        node.next = next_node.next


    def print_list(self):
        cur = self._head
        while cur:
            print("{:=^20}".format(cur.val))
            cur = cur.next
        print("---------------")


if __name__ == "__main__":
    l = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    l.add_node(n1)
    l.add_node(n2)
    l.add_node(n3)
    l.add_node(n4)
    l.add_node(n5)
    l.add_node(n6)
    l.add_node(n7)
    print(l.get_nth_node(4).val)
    l.delete_middle_node_without_head(l.get_nth_node(4))
    print(l.get_nth_node(4).val)
    l.delete_middle_node_without_head(l.get_nth_node(4))
    print(l.get_nth_node(3).val)
    l.delete_middle_node_without_head(l.get_nth_node(3))
    l.print_list()
