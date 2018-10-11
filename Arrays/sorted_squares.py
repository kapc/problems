#! /usr/env/python

def sorted_squares(nums):
    """

    :param nums:
    :return:
    """
    start = 0
    end = len(nums) - 1
    result = []

    while start < end:
        start_value = nums[start] ** 2
        end_value = nums[end] ** 2

        if start_value > end_value:
            result.insert(0, start_value)
            start += 1
        else:
            result.insert(0, end_value)
            end -= 1
    return result

print sorted_squares([-6, -2, 1, 3, 9])








