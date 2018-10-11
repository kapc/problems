#! /usr/env/python

"""
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
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

    def length(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def check_intersection(self, other_list):
        head1 = self._head
        head2 = other_list._head

        len1 = self.length()
        len2 = other_list.length()
        diff = abs(len1 - len2)

        if len1 > len2:
            while count < diff:
                head1 = head1.next
                count += 1
        elif len2 > len1:
            while count < diff:
                head2 = head2.next
                count += 1
        else:
            return head1 if head1 == head2 else None
        while head1 and head2:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        return None

    def print_list(self):
        cur = self._head
        while cur:
            print("{:=^20}".format(cur.val))
            cur = cur.next
        print("---------------")


if __name__ == "__main__":
    l = LinkedList()
    n1 = Node(1)
    n2 = Node(10)
    n3 = Node(4)
    n4 = Node(12)
    n5 = Node(6)

