#! /usr/env/python

"""
Palindrome: Implement a function to check if a linked list is a palindrome.
Hints: #5, #13, #29, #61, #101
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self._head = head
        self._node_dict = {}

    def add_node(self, new_node):
        if not self._head:
            self._head = new_node
            return
        new_node.next = self._head
        self._head = new_node

    def clone_list(self):
        cur = self._head
        new_list = LinkedList()
        new_head = None

        while cur:
            new_list.add_node(Node(cur.val))
            cur = cur.next
        return new_list

    def reverse_list(self):
        if not self._head:
            return None
        prev = None
        cur = self._head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self._head = prev

    def check_palindrom_helper(self, head1, head2):
        if not head2:
            return True, head1
        result, head1 = self.check_palindrom_helper(head1, head2.next)
        if not result:
            return False, None
        if head1.val != head2.val:
            return False, None
        return True, head1.next

    def check_palindrom(self):
        head1 = self._head
        head2 = self._head
        return self.check_palindrom_helper(head1, head2)

    def check_palindrom_with_copy(self):
        new_list = self.clone_list()
        new_list.print_list()
        start1 = self._head
        start2 = new_list._head
        while start1 and start2:
            if start1.val != start2.val:
                return False
            start1 = start1.next
            start2 = start2.next
        return True

    def print_list(self):
        cur = self._head
        while cur:
            print(cur.val)
            cur = cur.next
        print("====== ")


if __name__ == "__main__":
    l = LinkedList()
    l.add_node(Node(3))
    l.add_node(Node(2))
    l.add_node(Node(2))
    l.add_node(Node(2))
    l.add_node(Node(1))
    l.add_node(Node(2))
    l.add_node(Node(3))
    l.print_list()
    print(l.check_palindrom_with_copy())
