#! /usr/env/python
import random
"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C - > D -> E -> C [the same C as earlier)
Output: C

Input: a -> b -> c -> d -> e -> f -> c
Output: c 

Input: a -> b -> c -> d
Output: None

What is the expectation here?
"""

"""
Ask question,

1. Linkedlist must have a loop.
2. Are we allowed to have extra memory?
3. If the full list is givne here we should not have enough information here.
4. Finding a loop, 
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

    def print_list(self):
        cur = self._head
        while cur:
            print("{:=^20}".format(cur.val))
            cur = cur.next
        print("---------------")

    def _detect_loop(self):
        first = self._head
        second = self._head
        while first and second:
            if not second.next:
                return None
            first = first.next
            second = second.next.next
            if first == second:
                return first
        return None

    def _get_loop_size(self, loop_node):
        count = 0
        cur = loop_node.next
        while cur != loop_node:
            cur = cur.next
            count += 1
        return count

    def _get_length(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def get_loop_begining(self):
        if not self._head:
            return None

        loop_node = self._detect_loop()
        if loop_node:
            size_loop = self._get_loop_size(loop_node)
            length_list = self._get_length()
            count = abs(length_list - size_loop)
            cur = self._head
            while count:
                cur = cur.next
                count -= 1
            return cur
        return None

    def add_n_nodes(self, n):

        for i in range(0, n):
            val = random.randint(0, 100)
            self.add_node(Node(val))

    def make_loop(self, n):
        count = 0
        cur = self._head
        while count < n:
            cur = cur.next
            count += 1
        tail = self._head
        while tail.next:
            tail = tail.next
        tail.next = cur


if __name__ == "__main__":
    l = LinkedList()
    l.add_n_nodes(10)
    l.make_loop(3)
    print(l.get_loop_begining())

