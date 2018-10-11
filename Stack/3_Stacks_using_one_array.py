#! /usr/env/python

"""
 - Three in One: Describe how you could use a single array to implement three stacks.
        1. What is the size of each stack?
        2. Is this stack of ints or something else?

 - How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
        1. Stack on integers
        2. Can we have extra memory?
"""

class Stack(object):
    """
    Stack object.
    """
    def __init__(self, size, start_index, end_index, num_array):
        """

        :param size:
        """
        self._max_index = end_index
        self._size = size
        self._top = start_index - 1
        self._start_index = start_index
        self._nums = num_array

    def pop(self):
        """

        :return:
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        val = self._nums[self._top]
        self._top -= 1
        return val

    def is_empty(self):
        """

        :return:
        """
        return self._top == self._start_index - 1

    def is_full(self):
        """

        :return:
        """
        return self._top == self._max_index - 1

    def push(self, val):
        """

        :return:
        """
        if self.is_full():
            raise Exception("Stack Overflow")
        self._top += 1
        self._nums[self._top] = val

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


def test_stack(s):
    """

    :param s:
    :return:
    """
    arr = [i for i in range(100)]

    for i in range(0, 10):
        s.push(arr[i])

    index = i
    while not s.is_empty():
        val = s.pop()
        assert arr[index] == val, "%d %d" %(arr[index], val)
        index -= 1
    try:
        for i in range(50):
            s.push(arr[i])
    except Exception as e:
        print "Generated exception."
    else:
        assert False, "Failed to generate exception."

    index = 32
    while not s.is_empty():
        val = s.pop()
        assert arr[index] == val, "%d %d" %(arr[index], val)
        index -= 1

if __name__ == "__main__":

    # Problem 1.
    num_array = [0] * 99
    size_of_stack = len(num_array) / 3
    start_index = 0
    end_index = start_index + size_of_stack
    s1 = Stack(size_of_stack, start_index, end_index, num_array)
    start_index = end_index
    end_index = start_index + size_of_stack
    s2 = Stack(size_of_stack, start_index, end_index, num_array)
    start_index = end_index
    end_index = start_index + size_of_stack
    s3 = Stack(size_of_stack, start_index, end_index, num_array)

    test_stack(s1)
    test_stack(s2)
    test_stack(s3)

