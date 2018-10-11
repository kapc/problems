#! /usr/env/python

"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5)
       3 - 5 - 2 - 10 - 1 - 11 - 3
Output: 3
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

    def partition_list(self, part_val):
        start1 = None
        start2 = None
        head1 = None
        head2 = None

        cur = self._head
        while cur:
            next = cur.next
            cur.next = None
            if cur.val < part_val:
                if start1:
                    start1.next = cur
                    start1 = start1.next
                else:
                    start1 = cur
                    head1 = start1
            else:
                if start2:
                    start2.next = cur
                    start2 = start2.next
                else:
                    start2 = cur
                    head2 = start2
            cur = next
        start1.next = head2
        self._head = head1
        return

    def partition_list_short(self, part_val):
        head = self._head
        tail = self._head
        cur = self._head

        while cur:
            next = cur.next
            if cur.val < part_val:
                cur.next = head
                head = cur
            else:
                tail.next = cur
                tail = cur
            cur = next
        tail.next = None
        self._head = head
        return

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
    n6 = Node(16)
    n7 = Node(5)
    l.add_node(n1)
    l.add_node(n2)
    l.add_node(n3)
    l.add_node(n4)
    l.add_node(n5)
    l.add_node(n6)
    l.add_node(n7)
    l.print_list()
    l.partition_list(12)
    l.print_list()
