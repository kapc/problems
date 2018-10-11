"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
Hints: # 75, #32, #43
"""

from min_stack import Stack

"""

Clarifying Questions:
- Sorting to stack with integers
- Can use additional stack
- Is there limit on how many times we can call push/pop


Make examples:

34 1 23 45
1 23 34

temp stack: 

TestCases:
[1,2,3,4] => 1,2,3,4
[1] => [1]
[] => []
[1,3,2,4] => [1,2,3,4]
[1,1,1,1] => [1,1,1,1]
"""

class SortedStack(object):
    """
    SortedStack class.
    """
    def __init__(self):
        """

        """
        self._main_stack = Stack()
        self._temp_stack = Stack()

    def push(self, value):
        """

        :param value:
        :return:
        """
        done = False
        if self._main_stack.is_empty():
            self._main_stack.push(value)
            return
        cur_top = self._main_stack.peek()
        if value >= cur_top:
            while not self._main_stack.is_empty():
                self._temp_stack.push(self._main_stack.pop())
        else:
            self._main_stack.push(value)
            return
        while not self._temp_stack.is_empty():
            cur_top = self._temp_stack.pop()
            if value >= cur_top:
                self._main_stack.push(value)
            self._main_stack.push(cur_top)
        assert self._temp_stack.is_empty(), "Failure, tmp stack not empty."

    def pop(self):
        return self._main_stack.pop()

    def peek(self):
        return self._main_stack.peek()

    def is_empty(self):
        return self._main_stack.is_empty()

if __name__ == "__main__":
    arr_inputs = [[56, 12, 34, 44, 99, 56, 22, 89, 78], [1], [], [1,2,3,4], [4,3,2,1], [1,1,1,1]]
    result = []
    expected_results = [[12, 22, 34, 44, 56, 56, 78, 89, 99], [1], [], [1,2,3,4], [1,2,3,4], [1,1,1,1]]

    for i in range(0, len(arr_inputs)):
        arr_input = arr_inputs[i]
        expected_result = expected_results[i]
        s = SortedStack()

        for x in arr_input:
            s.push(x)
        while not s.is_empty():
            result.append(s.pop())
        assert result == expected_result, "Failure %s %s " %(str(result), str(expected_result))
        result = []




