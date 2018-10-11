#! /usr/env/python

"""
Power Set: Write a method to return all subsets of a set.

(1,2,3) = [(), (1), (2), (3), (1,2), (1,3), (2,3), (1,2,3)]
() = ()
(1) = [(), (1)]
(1,1) => [(), (1), (1), (1,1)]
"""


def subsets_of_set_helper(first, rest, set_till_now, results):
    """

    :param nums:
    :return:
    """
    if not rest:
        return
    for i in range(0, len(rest)):
        subsets_of_set_helper(first, rest[i+1:], set_till_now + [rest[i]], results)
        results.append(set_till_now + [rest[i]])


def subsets_of_set(nums):
    """
    Print subsets of set.
    :param nums:
    :return:
    """
    results = []
    subsets_of_set_helper([], nums, [], results)
    print results

def subset_with_dup(self, first, rest, idx, result):
        """
        """
        result.append(first)
        if not rest:
            return

        for i in range(idx, len(rest)):
            if i > 0 and rest[i] == rest[i - 1]:
                continue
            self.subset_with_dup(first + [rest[i]], rest[0:i] + rest[i + 1:], i, result)

def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        first = []
        rest = sorted(nums)
        result = []

        self.subset_with_dup(first, rest, 0, result)
        return result

"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using the
* operator. You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
Hints: # 166, #203, #227, #234, #246, #280
"""

def mult_val(num1, num2):
    """

    :param num1:
    :param num2:
    :return:
    """
    shift_value = 1

    while (shift_value << 1) < num2:
        shift_value  = shift_value << 1

    





if __name__ == "__main__":
    sets_a = [0, 1, 2]
    results = [[], [0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]]
    subsets_of_set(sets_a)
    print_val(8)



