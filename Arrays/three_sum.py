#! /usr/env/python

class Solution(object):
    def two_sum(self, nums, start, end, start_elem, target):
        """
        """
        result = []
        if start > end:
            return result
        while start < end:
            cur_sum = nums[start] + nums[end]
            if cur_sum == target:
                result.append([start_elem] + [nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
            elif cur_sum < target:
                start += 1
            else:
                end -= 1
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        start = 0
        end = len(nums) - 1
        nums.sort()
        result = []

        for i in range(0, len(nums)):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            result += self.two_sum(nums, i + 1, end, nums[i], target)
        return result
