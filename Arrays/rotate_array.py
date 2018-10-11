#! /usr/env/python

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

def rotate_array_by_copy(nums, k):
    """

    :param nums:
    :return:
    """
    len_nums = len(nums)
    result = []
    if k > len_nums:
        k = k % len_nums
    start_index = len_nums - k
    for i in range(start_index, len_nums):
        result.append(nums[i])
    for i in range(0, start_index):
        result.append(nums[i])
    return result

def rotate_array_in_place_dumb(nums, k):
    """

    :param nums:
    :param k:
    :return:
    """
    if not nums:
        return []
    if k > len(nums):
        k = k % len(nums)
    for i in xrange(k):
        tmp = None
        for i in range(0, len(nums)):
            if not tmp:
                tmp = nums[i]
            else:
                next = nums[i]
                nums[i] = tmp
                tmp = next
        nums[0] = tmp

def reverse(nums, start, end):
    """

    :param nums:
    :param start:
    :param end:
    :return:
    """
    if start >= end:
        return nums
    while start < end:
        tmp = nums[start]
        nums[start] = nums[end]
        nums[end] = tmp
        start += 1
        end -= 1

    return nums

def rotate_array_in_place(nums, k):
    """

    :param nums:
    :param k:
    :return:
    """
    if not nums:
        return []

    if k > len(nums):
        k = k % len(nums)

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)


def test():
    """"
    """
    test_inputs = [([1,2,3,4,5,6,7], 3), ([], 1), ([1,2,3,4], 6), ([2147483647,-2147483648,33,219,0], 4)]

    for test_input in test_inputs:
        nums, k = test_input
        rotate_array_in_place(nums, k)
        print nums

test()