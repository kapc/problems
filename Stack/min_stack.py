#! /usr/env/python

"""
 - Three in One: Describe how you could use a single array to implement three stacks.
        1. What is the size of each stack?
        2. Is this stack of ints or something else?

 - How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
        1. Stack on integers
        2. Can we have extra memory?
        3. Can stack have dups?
"""

class Stack(object):
    """
    Stack object.
    """
    def __init__(self):
        """

        :param size:
        """
        self._top = -1
        self._nums = []

    def pop(self):
        """

        :return:
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        self._top -= 1
        return self._nums.pop()

    def print_stack(self):
        print(self._nums)

    def is_empty(self):
        """

        :return:
        """
        return self._top == -1

    def push(self, val):
        """

        :return:
        """
        self._nums.append(val)
        self._top += 1

    def peek(self):
        """

        :return:
        """
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self._nums[self._top]

    def top(self):
        """

        :return:
        """
        return self._top

class MinStack(object):
    """

    """
    def __init__(self):
        """

        :param main_stack:
        :param min_stack:
        """
        self._main_stack = Stack()
        self._min_stack = Stack()

    def is_empty(self):
        return self._main_stack.is_empty() and self._min_stack.is_empty()

    def is_full(self):
        return self._main_stack.is_full()

    def push(self, val):
        if self._min_stack.is_empty():
            self._min_stack.push(val)
        else:
            cur_min = self._min_stack.peek()
            if val <= cur_min:
                self._min_stack.push(val)
        self._main_stack.push(val)

    def print_stack(self):
        self._min_stack.print_stack()
        self._main_stack.print_stack()

    def pop(self):
        val = self._main_stack.pop()
        cur_min = self._min_stack.peek()
        if val == cur_min:
            self._min_stack.pop()
        return val

    def min(self):
        return self._min_stack.peek()

    def top(self):
        return self._main_stack.peek()



if __name__ == "__main__":

    # Problem 2:
    input = [33,44,55,1,99,2,110,22,-100,9]
    s = MinStack()
    for x in input:
        s.push(x)

    assert -100 == s.min()
    for i in range(2):
        s.pop()
    assert 1 == s.min()
    for i in range(5):
        s.pop()
    assert 33 == s.min()
    s = MinStack()
    s.push(1)
    s.push(1)
    s.push(2)

