#! /usr/env/python

"""
Magic Index: A magic index in an array A [e ... n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
Hints: # 170, #204, #240, #286, #340

Examples:
    [0, 1, 2] => true
    [0] => True
    [-100, -23, -1, 0, 1, 2, 3, 4, 5, 9] => True

"""

def find_magic_index_search(nums, start, end):
    """

    :param nums:
    :param start:
    :param end:
    :return:
    """

    if start > end:
        return False

    mid_index = start + (end - start) / 2
    mid_val = nums[mid_index]

    if mid_index > mid_val:
        return find_magic_index_search(nums, mid_index + 1, end)
    elif mid_index < mid_val:
        return find_magic_index_search(nums, start, mid_index - 1)

    return True



def find_magic_index(nums):
    """

    :param nums:
    :return:
    """
    return find_magic_index_search(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    test_inputs = [[], [0], [1], [0, 1], [1, 2], [-100, -23, -1, 0, 1, 2, 3, 4, 5, 9]]
    test_results = [False, True, False, True, False, True]

    for i in range(0, len(test_inputs)):
        assert find_magic_index(test_inputs[i]) == test_results[i]



