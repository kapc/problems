#! /usr/env/python

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

class Solution(object):

    def reverse_list(self, nums, start, end):
        """
        """

        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur_index = -1
        target_index = -1

        for idx in range(len(nums) - 1, 0, -1):
            if idx > 0 and nums[idx] > nums[idx - 1]:
                cur_index = idx - 1
                break

        for idx in range(cur_index + 1, len(nums)):
            if nums[idx] > nums[cur_index]:
                target_index = idx
        if cur_index != -1:
            tmp = nums[cur_index]
            nums[cur_index] = nums[target_index]
            nums[target_index] = tmp

        self.reverse_list(nums, cur_index + 1, len(nums) - 1)