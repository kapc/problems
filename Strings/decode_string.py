#! /usr/env/python

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


    226

       2      22
     2  26     6
    6

"""

def lookup(num):
    """

    :param digit:
    :return:
    """
    num = int(num)
    return chr(ord('A') + num - 1)



def decode_helper(in_str, max_len, result_till_now, result):
    """

    :param in_str:
    :param result_till_now:
    :param result:
    :return:
    """
    if not in_str:
        result.append(result_till_now)
        return


    decode_helper(in_str[1:], max_len, result_till_now + lookup(in_str[0]), result)
    if in_str[1:] and int(in_str[0:2]) <= 26 and int(in_str[0:2]) >= 0:
        decode_helper(in_str[2:], max_len, result_till_now + lookup(in_str[0:2]), result)


def decode(in_str):
    """

    :param in_str:
    :return:
    """
    result = []

    if not in_str:
        raise Exception("Invalid String")
    decode_helper(in_str, len(in_str), "", result)
    return len(result)


decode("226")
decode("1")
decode("12332344342343244")
