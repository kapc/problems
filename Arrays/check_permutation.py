#! /usr/env/python

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

"""
1. sort both the strings in the lexicographical order and compare.
"""

def check_permutation(str1, str2):
    """

    :param str1:
    :param str2:
    :return:
    """
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    return str1 == str2

def get_all_permutations_helper(first, rest, result):
    """

    :param first:
    :param rest:
    :param result:
    :return:
    """
    if not rest:
        result.append(first)
        return
    for i in range(0, len(rest)):
        c = rest[i]
        get_all_permutations_helper(first + c, rest[:i] + rest[i+1:], result)

def get_all_permutations(str1):
    """

    :param str1:
    :return:
    """
    result = []
    get_all_permutations_helper("", str1, result)
    return result

def check_permutation2(str1, str2):
    """

    :param str1:
    :param str2:
    :return:
    """
    if len(str1) != len(str2):
        return False
    if len(str1) < len(str2):
        result = get_all_permutations(str1)
        if str2 in result:
            return True
    else:
        result = get_all_permutations(str2)
        if str1 in result:
            return True
    return False

def check_permutation3(str1, str2):
    """

    :param str1:
    :param str2:
    :return:
    """
    str_map = [0] * 128
    if len(str1) != len(str2):
        return False
    for i in range(0, len(str1)):
        c = str1[i]
        str_map[ord(c)] += 1

    for j in range(0, len(str2)):
        c = str2[j]
        str_map[ord(c)] -= 1
        if str_map[ord(c)] < 0:
            return False
    return True




if __name__ == "__main__":
    assert check_permutation("abc", "acb")
    assert check_permutation("abcd", "asdf") == False
    assert check_permutation2("abc", "acb")
    assert check_permutation2("abcd", "asdf") == False
    assert check_permutation("", "")
    assert check_permutation2("", "")
    assert check_permutation("a", "a")
    assert check_permutation2("a", "a")
    assert check_permutation3("abc", "bac")
    assert check_permutation3("abcd", "abc") == False
