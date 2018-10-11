#! /usr/env/python

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 1
        high = x

        if x < 1:
            return 0

        while low < high:
            mid = low + (high - low) / 2
            target = mid * mid
            next_elem = mid + 1
            prev_elem = mid - 1

            if target == x:
                return mid
            elif target < x:
                if next_elem * next_elem > x:
                    return mid
                low = mid
            else:
                if prev_elem * prev_elem < x:
                    return prev_elem
                high = mid
        return low
