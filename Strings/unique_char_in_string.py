#! /usr/env/python

"""
First Unique Character in a String
Difficulty:Easy

Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

def find_first_non_repeating_char(in_str):
    """

    :param in_str:
    :return:
    """
    char_map = {}
    for c in in_str:
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1

    for i in range(0, len(in_str)):
        c = in_str[i]
        if char_map[c] == 1:
            return i
    return -1

def test():
    test_inputs = ["chandresh", "aaaaaaa", "", "d46wxxta@33"]
    results = [0, -1, -1, 0]
    for i in range(0, len(test_inputs)):
        assert results[i] == find_first_non_repeating_char(test_inputs[i])
