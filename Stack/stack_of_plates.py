#! /usr/env/python

"""
3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific substack.
"""

class StackFullException(Exception):
    pass
class StackEmptyException(Exception):
    pass

class Stack:
    def __init__(self, size):
        self._size = size
        self._elems = []

    def push(self, elem):
        if self.is_full():
            raise StackFullException("Stack is full.")
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("Stack is empty.")
        return self._elems.pop()

    def is_empty(self):
        return len(self._elems) == 0

    def is_full(self):
        return len(self._elems) >= self._size

    def __repr__(self):
        return "{}".format(self._elems)

class SetOfStacks:
    def __init__(self, max_stacks=10):
        self._max_stacks = max_stacks
        self._stack_list = [Stack(10)]
        self._bottom_stack = 0

    def push(self, elem):
        cur_stack = self._stack_list[self._bottom_stack]
        if cur_stack.is_full():
            if len(self._stack_list) == self._max_stacks:
                raise StackFullException()
            self._stack_list.append(Stack(10))
            self._bottom_stack += 1
        cur_stack = self._stack_list[self._bottom_stack]
        cur_stack.push(elem)

    def pop(self):
        cur_stack = self._stack_list[self._bottom_stack]
        if cur_stack.is_empty():
            self._bottom_stack -= 1
            cur_stack = self._stack_list[self._bottom_stack]
        if cur_stack.is_empty():
            raise StackEmptyException()
        return cur_stack.pop()


s = SetOfStacks()

for i in range(0, 50):
    s.push(i)

