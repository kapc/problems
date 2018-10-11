#! /usr/env/python

"""
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .Thatis,617 + 295.
Output: 2 - > 1 - > 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
Output: 9 - > 1 - > 2. That is, 912.
"""

"""
Questions:
1. Can be empty list?
2. Number with different length?
3. Sum as result?
4. Integers only?
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
        print("Adding {}".format(new_node.val))
        if not self._head:
            self._head = new_node
            return
        new_node.next = self._head
        self._head = new_node

    def print_list(self):
        cur = self._head
        while cur:
            print(cur.val)
            cur = cur.next

def sum_list_recursive_helper(l1, l2, result, carry):
    if not l1 and not l2:
        return
    value = carry
    if l1:
        value += l1.val
    if l2:
        value += l2.val

    carry = int(value / 10)
    digit = int(value % 10)

    result.add_node(Node(digit))
    sum_list_recursive_helper(l1.next if l1 else None, l2.next if l2 else None, result, carry)

def sum_list_recursive(list1, list2):
    result = LinkedList()
    sum_list_recursive_helper(list1._head, list2._head, result, 0)
    return result

def sum_list(list1, list2):

    l = LinkedList()
    l1 = list1._head
    l2 = list2._head

    if not l1:
        return l2
    if not l2:
        return l1

    head = None
    cur = None
    leftover = 0

    while l1 and l2:
        digit = (l1.val + l2.val + leftover) % 10
        leftover = int((l1.val + l2.val + leftover) / 10)
        l.add_node(Node(digit))
        if not cur:
            head = cur
        else:
            cur = cur.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        l.add_node(Node(l1.val + leftover))
        l1 = l1.next
        leftover = 0

    while l2:
        l.add_node(Node(l2.val + leftover) )
        l2 = l2.next
        leftover = 0

    if leftover:
        l.add_node(Node(leftover))

    return l

def generate(num):
    l = LinkedList()
    while num:
        cur = num % 10
        l.add_node(Node(cur))
        num = int(num / 10)
    return l

if __name__ == "__main__":
    l1 = generate(716)
    l1.print_list()
    l2 = generate(592)
    l2.print_list()
    print("==================")
    l = sum_list_recursive(l1, l2)
    l.print_list()
