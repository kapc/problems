#! /usr/env/python

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.

"""

class Solution(object):

    def get_hamming_distance(self, num):
        """
        """
        count = 0
        while num:
            if num & 1 == 1:
                count += 1
            num = num >> 1

        return count

    def get_hamming_distance_helper(self, num, cache):
        """
        """
        count = 0
        while num:
            num_bits = num & 0xF
            count += cache[num_bits]
            num = num >> 4

        return count

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_count = 0

        cache = [0] * 16
        for i in range(0, 16):
            count = self.get_hamming_distance(i)
            cache[i] = count

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    num = nums[i] ^ nums[j]
                    total_count += self.get_hamming_distance_helper(num, cache)
        return total_count


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_count = 0
        count = [0 for i in xrange(32)]
        length = len(nums)

        for i in range(0, len(nums)):
            num = nums[i]
            j = 0
            while num:
                count[j] += num & 1
                num = num >> 1
                j += 1

        for i in xrange(32):
            total_count += count[i] * (length - count[i])

        return total_count