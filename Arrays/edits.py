#! /usr/env/python

"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, pIe -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false

pale => ple
pale => plle
pale => plleee

"""

def find_one_edit_away(in_str, target_str):
    """

    :param in_str:
    :param target_str:
    :return:
    """
    if abs(len(in_str) - len(target_str)) > 1:
        return False
    idx = 0
    count = 0
    while idx < len(in_str):
        if idx > len(target_str) - 1:
            count += 1
            idx += 1
            continue
        if in_str[idx] != target_str[idx]:
            count += 1
        idx += 1
    if idx < len(target_str) - 1:
        count += 1
        idx += 1
    return count <= 1

if __name__ == "__main__":
    assert find_one_edit_away("abc", "cab") == False
    assert find_one_edit_away("abcd", "abc")
    assert find_one_edit_away("abd", "abddddd") == False
    assert find_one_edit_away("", "")
    assert find_one_edit_away("", "abd") == False
    assert find_one_edit_away("pales", "pale")
    assert find_one_edit_away("bale", "pale")

