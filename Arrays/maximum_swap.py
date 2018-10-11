#! /usr/env/python

"""
Maximum Swap
Difficulty:Medium

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]

"""

def maximum_swap(num):
        """
        :type num: int
        :rtype: int
        """
        num_str = list(str(num))
        start = 0
        end = len(num_str) - 1

        for i in range(0, len(num_str)):
            digit1 = int(num_str[i])
            digit2 = -1
            index = -1
            for j in range(i+1, len(num_str)):
                if int(num_str[j]) >= digit2:
                    digit2 = int(num_str[j])
                    index = j
            if digit1 < digit2:
                tmp = num_str[i]
                num_str[i] = num_str[index]
                num_str[index] = tmp
                return int("".join(num_str))
        return int("".join(num_str))


def test_maximum_swap():
    """

    :return:
    """
    inputs = [99991, 2945, 10000, 19292, 0, 101921]
    for i in inputs:
        print maximum_swap(i)

test_maximum_swap()