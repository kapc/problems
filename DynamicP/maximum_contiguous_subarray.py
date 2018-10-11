#! /usr/env/python

def max_contiguous_subarray(nums):
    """
    :return:
    """
    dp = [0 for x in nums]
    if not nums:
        return -1

    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])

    return max(dp)

print max_contiguous_subarray([-2, 9, -11, 3, 2,5,-1, -5, 4])
