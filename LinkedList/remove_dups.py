#! /usr/env/python

"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

"""
Questions:
1. Linkedlist is of integers?
2. Unsorted.

Examples:
1.
1 -> 2 -> 3 -> 2
1 -> 2 -> 3
2.
1 -> 1 -> 1
1
3.
NONE
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

    def remove_dups(self):
        if not self._head:
            return
        prev = None
        cur = self._head
        while cur:
            if cur.val not in self._node_dict:
                self._node_dict[cur.val]  = True
                prev = cur
            else:
                prev.next = cur.next
            cur = cur.next

    def remove_dups_without_dict(self):
        if not self._head:
            return
        ptr1 = self._head
        while ptr1:
            prev = ptr1
            ptr2 = prev.next
            while ptr2:
                if ptr2.val == ptr1.val:
                    prev.next = ptr2.next
                else:
                    prev = ptr2
                ptr2 = ptr2.next
            ptr1 = ptr1.next

    def print_list(self):
        cur = self._head
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    l = LinkedList()
    l.add_node(Node(1))
    l.add_node(Node(1))
    l.add_node(Node(2))
    l.add_node(Node(1))
    l.add_node(Node(1))

    l.print_list()
    print("{:=^20}".format("Before removal."))
    l.print_list()
    l.remove_dups_without_dict()
    print("{:=^20}".format("After removal."))
    l.print_list()





