#! /usr/env/python

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

"""
Approach 1:
Sort nlogn and then do  linear scan.
"""

"""
Approach 2:
- Add all elements into a hashtable
- Only scan sequences which starts at this number. If the previous number is in hashtable, this is part of another
big sequence so ignore it.
"""

def longest_consecutive_sequence(nums):
    """

    :return:
    """
    num_len = len(nums)
    hash_set = {}
    max_count = 0
    i = 0

    for num in nums:
        hash_set[num] = True

    while i < num_len:
        if nums[i]-1 not in hash_set:
            cur_num = nums[i]
            cur_count = 1
            while cur_num + 1 in hash_set:
                cur_count += 1
                cur_num += 1
                i += 1
            max_count = max(max_count, cur_count)
        i += 1

    return max_count

print longest_consecutive_sequence([100, 2, 1, 4, 3, 5, -1, -3, -2, 0])
print longest_consecutive_sequence([0,9,1,1,1,1,1,1,1,1])


