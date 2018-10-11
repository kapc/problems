#! /usr/env/python

# Given a sequence, find the length of the longest palindromic subsequence in it.

def longest_palindrom(in_str):
    """

    :param in_str:
    :return:
    """
    return lps(in_str, 0, len(in_str) - 1)

def lps(in_str, i, j):
    """

    :param in_str:
    :param i:
    :param j:
    :return:
    """
    if i == j:
        return 1

    if in_str[i] == in_str[j] and i+1 == j:
        return 2

    if in_str[i] == in_str[j]:
        return lps(in_str, i+1, j-1) + 2

    return max(lps(in_str, i+1, j), lps(in_str, i, j-1))


def longest_palindrom_dp(in_str):
    """

    :param in_str:
    :return:
    """
    n = len(in_str)
    table = [[0 for i in xrange(len(in_str))] for j in xrange(len(in_str))]
    for i in range(0, n):
        table[i][i] = 1

    for cl in range(2, n+1):
        for i in range(0, n-cl+1):
            j = i + cl - 1
            if in_str[i] == in_str[j] and cl == 2:
                table[i][j] = 2
            elif in_str[i] == in_str[j]:
                table[i][j] = table[i+1][j-1] + 2
            else:
                table[i][j] = max(table[i][j-1], table[i+1][j])
    print table
    return table[0][n-1]



print longest_palindrom_dp("abadaba")

